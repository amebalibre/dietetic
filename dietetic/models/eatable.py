"""eatable."""

from odoo import api
# from odoo.exceptions import UserError
from odoo import fields
from odoo import models


class Eatable(models.Model):
    """eatable."""

    _name = 'eatable'

    name = fields.Char(
        required=True,
    )

    type_id = fields.Many2one(
        string='Type',
        comodel_name='type',
        required=True,
    )

    is_ingredient = fields.Boolean(
        string='Is Ingredient',
        compute='_compute_is_ingredient',
        store=True,
    )

    color = fields.Integer()

    price = fields.Float()

    amount = fields.Float(
        default=0,
        # required=True,
    )

    measure_id = fields.Many2one(
        string='Measure',
        comodel_name='measure',
        # required='True',
    )

    description = fields.Text(
        string='Info'
    )

    category_ids = fields.Many2many(
        string='Categories',
        comodel_name='category',
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

    # Not stored. Only needed for compute 'season_ids'
    # field with edition enabled
    computed_season_ids = fields.Many2many(
        comodel_name='season',
        compute='_compute_season_ids',
        store=False,
    )

    image = fields.Char(
        default='Not found!'
    )

    url = fields.Char()

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

        # Set category_ids
        for record in self:
            category_ids = \
                record.eatable_ids.mapped('name').mapped('category_ids')
            record.category_ids = category_ids if category_ids else False


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
