"""price."""

from odoo import fields
from odoo import models


class Price(models.Model):
    """price."""

    _name = 'price'

    name = fields.Float(
        string='amount',
        required=True
    )

    eatable_id = fields.Many2one(
        comodel_name='eatable',
        # required=True,
    )

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        # required=True,
    )

    country_id = fields.Many2one(
        comodel_name='res.country',
        # required=True,
    )
