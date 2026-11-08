
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    # Task 3
    # Delivery Information
    customer_po_number = fields.Char(string="Customer Purchase Order")
    expected_delivery_date = fields.Date(string="Expected Delivery Date")
    delivery_priority = fields.Selection([
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('very urgent', 'Very Urgent'),
    ],
        default='normal', string="Delivery Priority")

    requires_installation = fields.Boolean(string="Requires Installation?")
    delivery_notes = fields.Text(string="Special Delivery Instructions")

    @api.constrains('expected_delivery_date', 'date_order')
    def _check_expected_delivery_date(self):
        for record in self:
            if record.expected_delivery_date and record.date_order:
                order_date = fields.Date.to_date(record.date_order)

                if record.expected_delivery_date < order_date:
                    raise ValidationError(
                        "Expected delivery date cannot be earlier than the order date."
                    )

    def action_confirm(self):
        for record in self:
            if not record.expected_delivery_date:
                raise ValidationError(
                    "Please set Expected Delivery Date before confirming the quotation."
                )

        return super().action_confirm()
