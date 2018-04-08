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

    color = fields.Integer()

    price = fields.Float(
        string='Price',
    )

    computed_price = fields.Float(
        string='Price',
        compute='_compute_eatable_ids',
        store=True,
    )

    description = fields.Text()

    category_ids = fields.Many2many(
        comodel_name='category',
    )

    # eatable_ids = fields.Many2many(
    #     comodel_name='eatable',
    # )

    eatable_ids = fields.One2many(
        string='Ingredients',
        comodel_name='eatable_eatable_rel',
        inverse_name='eatable_id',
    )

    season_ids = fields.Many2many(
        string='Season',
        comodel_name='season',
    )

    # price_ids = fields.One2many(
    #     comodel_name='price',
    #     inverse_name='eatable_id',
    #     # compute='_compute_price',
    # )

    image = fields.Char(
        default='Not found!'
    )

    url = fields.Char()

    @api.depends('eatable_ids')
    def _compute_eatable_ids(self):
        if self.eatable_ids and len(self.eatable_ids) > 0:
            prices = []
            for eatable_id in self.eatable_ids.mapped('name'):
                prices.append(eatable_id.price)

            self.computed_price = sum(prices)
            self.price = self.computed_price

        else:
            self.computed_price = 0

    # @api.model
    # def create(self, vals):
    #     if self.computed_price:
    #         self.price = self.computed_price
    #
    #     return super(Eatable, self).create(vals)
    #
    # @api.model
    # def write(self, vals):
    #     if self.computed_price:
    #         self.price = self.computed_price
    #
    #     return super(Eatable, self).write(vals)

    # @api.depends('price')
    # def _compute_price(self):
    # @api.model
    # def create(self, vals):
    #     """create."""
    #
    #     eatable_id = super(Eatable, self).create(vals)
    #
    #     # self.env['price'].create({
    #     #     'name': self.price,
    #     #     'eatable_id': self.id,
    #     # })
    #
    #     # price_ids = self.env['price'].search([
    #     #     ('eatable_id', '=', eatable_id.id)
    #     # ])
    #
    #     amounts = [
    #         amount for amount in self.price_ids.mapped('name')
    #     ].append(eatable_id.price)
    #
    #     average = sum(amounts) / len(amounts) if amounts else 0.0
    #
    #     raise UserError('%s %s' % (average, amounts))
    #
    #     self.write({
    #         'price': average
    #     })
    #
    #     return eatable_id
