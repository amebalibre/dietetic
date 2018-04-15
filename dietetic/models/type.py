"""type."""

from odoo import fields
from odoo import models


class Type(models.Model):
    """Type."""

    _name = 'type'
    _order = 'order'

    name = fields.Char(
        string='Type',
        required=True,
        readonly=True,
    )

    acronym = fields.Char(
        string='Acronym',
        readonly=True,
    )

    order = fields.Integer(
        required=True,
        readonly=True,
    )

    eatable_ids = fields.Many2many(
        comodel_name='eatable',
    )

    _sql_constraints = [
        ('unique_measure', 'unique(name)', "Measure must be unique!")
    ]
