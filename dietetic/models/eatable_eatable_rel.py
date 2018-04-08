"""eatable_eatable_rel."""

from odoo import fields
from odoo import models


class EatableEatableRel(models.Model):
    """eatable_eatable_rel."""

    _name = 'eatable_eatable_rel'

    name = fields.Many2one(
        comodel_name='eatable',
        required='True',
        ondelete='cascade',
    )

    amount = fields.Float(
        default=0,
        required=True,
    )

    unit_amount = fields.Selection(
        selection=[
            ('unit', 'Unit'),
            ('gr', 'Grams'),
            ('ml', 'Mililiters'),
            ('cup', 'Cup'),
            ('spoon', 'Spoon'),
            ('tspoon', 'Teaspoonful'),
        ],
        required='True',
    )

    eatable_id = fields.Many2one(
        comodel_name='eatable',
        required='True',
        ondelete='cascade',
        editable=False,
    )

    _sql_constraints = [
        ('eatable_eatable_rel_not_zero_measeure', 'check(amount > 0)',
         "The amount can't be zero or less!")
    ]
