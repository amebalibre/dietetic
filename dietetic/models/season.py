"""season."""

from odoo import fields
from odoo import models


class Season(models.Model):
    """Season."""

    _name = 'season'

    name = fields.Char(
        string='Season',
        required=True,
    )

    order = fields.Integer(
        required=True,
    )

    color = fields.Integer(
        default=1,
        readonly=True,
    )

    eatable_ids = fields.Many2many(
        comodel_name='eatable',
    )

    _sql_constraints = [
        ('unique_season', 'UNIQUE(name)',
         "Season must be unique!"),
        ('unique_season_order', 'UNIQUE(order)',
         "Order must be unique!"),
        ('greater_season_range', 'CHECK(order < 0)',
         "Order must be greater than zero!"),
        ('lower_season_range', 'CHECK(order >= 12)',
         "Order must be lower or equals than twelve!"),
    ]
