"""measure."""

from odoo import fields
from odoo import models


class Measure(models.Model):
    """Measure."""

    _name = 'measure'
    _order = 'order'

    name = fields.Char(
        string='Measure',
        required=True,
    )

    acronym = fields.Char(
        string='Acronym',
    )

    order = fields.Integer(
        required=True,
    )

    eatable_ids = fields.Many2many(
        comodel_name='eatable',
    )

    _sql_constraints = [
        ('unique_measure', 'unique(name)', "Measure must be unique!")
    ]
