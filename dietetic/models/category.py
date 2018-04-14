"""category."""

from odoo import fields
from odoo import models


class Category(models.Model):
    """Category."""

    _name = 'category'
    _order = 'order'

    name = fields.Char(
        string='Category',
        required=True,
        readonly=True,
    )

    order = fields.Integer(
        required=True,
        readonly=True,
    )

    color = fields.Integer(
        required=True,
        readonly=True,
    )

    eatable_ids = fields.Many2many(
        comodel_name='eatable',
    )

    _sql_constraints = [
        ('unique_category', 'unique(name)', "Category must be unique!")
    ]
