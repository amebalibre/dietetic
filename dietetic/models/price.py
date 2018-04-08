"""price."""

# from odoo import api
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
        # default='EUR',
        # required=True,
    )

    country_id = fields.Many2one(
        comodel_name='res.country',
        # default='Europe',
        # required=True,
    )

    # type_holder_id = fields.Many2one(
    #     string='Type Owner',
    #     comodel_name='pentec.type_holder'
    # )
