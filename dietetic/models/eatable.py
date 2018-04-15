"""eatable."""

from odoo import api
# from odoo.exceptions import UserError
from odoo import fields
from odoo import models


class Eatable(models.Model):
    """eatable."""

    _name = 'eatable'
    _order = 'is_ingredient, name'

    name = fields.Char(
        required=True,
    )

    amount = fields.Float(
        default=0,
    )

    color = fields.Integer()

    description = fields.Html(
        string='Info'
    )

    image = fields.Char(
        default='Not found!'
    )

    is_ingredient = fields.Boolean(
        string='Is Ingredient',
        compute='_compute_is_ingredient',
        store=True,
    )

    price = fields.Float()

    url = fields.Char()

    measure_id = fields.Many2one(
        string='Measure',
        comodel_name='measure',
        # required='True',
    )

    type_id = fields.Many2one(
        string='Type',
        comodel_name='type',
        required=True,
    )

    category_ids = fields.Many2many(
        string='Categories',
        comodel_name='category',
    )

    # Not stored. Only needed for compute 'season_ids'
    # field with edition enabled
    computed_season_ids = fields.Many2many(
        comodel_name='season',
        compute='_compute_season_ids',
        store=False,
    )

    eatable_ids = fields.One2many(
        string='Ingredients',
        comodel_name='eatable_eatable_rel',
        inverse_name='eatable_id',
    )

    season_ids = fields.Many2many(
        string='Season',
        comodel_name='season',
    )

    _sql_constraints = [
        ('check_measeure_amount', 'check(amount >= 0)',
         "The amount can't be less to zero!")
    ]

    @api.depends('type_id')
    def _compute_is_ingredient(self):
        for record in self:
            record.is_ingredient = not record.type_id or (
                record.type_id
                and record.type_id.name in ('Ingredient', 'Ingredient (Demo)')
            )
            if not record.is_ingredient:
                measure_id = self.env['measure'].search([
                    ('name', '=', 'Grams')
                ])
                record.measure_id = (4, measure_id) if measure_id else False

    # TODO(UPGRADE): un-efficiently on: Set season_ids
    @api.depends('eatable_ids')
    def _compute_season_ids(self):
        """Generate the season from the ingredients.

        Only adds season from ingredients if this seasons are the same between
        ingredients.
        """
        # Set season_ids
        ids = []
        for eatable_id in self.eatable_ids.mapped('name'):
            for season_id in eatable_id.season_ids:
                ids.append(season_id.id)
        if ids:
            tmp = set([x for x in ids if ids.count(x) > 1])
            if tmp:
                ids = tmp
            self.season_ids = self.env['season'].search([
                ('id', '=', ids)
            ])
        else:
            self.season_ids = False

        # Set category_ids
        for record in self:
            category_ids = \
                record.eatable_ids.mapped('name').mapped('category_ids')
            record.category_ids = category_ids if category_ids else False

        # Set price_ids
        for record in self:
            price_ids = record.eatable_ids.mapped('price')
            record.price = sum(price_ids) if price_ids else False


class EatableEatableRel(models.Model):
    """eatable_eatable_rel."""

    _name = 'eatable_eatable_rel'

    name = fields.Many2one(
        comodel_name='eatable',
        ondelete='cascade',
        required=True,
    )

    eatable_id = fields.Many2one(
        comodel_name='eatable',
        ondelete='cascade',
        required=True,
        readonly=True,
    )

    amount = fields.Float(
        default=0,
        required=True,
    )

    price = fields.Float(
        readonly=True,
        compute='_compute_price',
        store=True,
        help='Price of amount of the product',
    )

    measure_id = fields.Many2one(
        string='Measure',
        comodel_name='measure',
        related='name.measure_id',
        readonly=True,
    )

    _sql_constraints = [
        ('check_measeure_measure_rel_amount', 'check(amount >= 0)',
         "The amount can't be less to zero!")
    ]

    @api.depends('amount')
    def _compute_price(self):
        for record in self:
            if record.name.amount:
                record.price = \
                    (record.name.price / record.name.amount) * record.amount
