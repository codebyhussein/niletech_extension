
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from pkg_resources import require


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    # Task 1
    # Add new fields to the product template model

    warranty_period = fields.Integer(string="Warranty Period (in months)")
    brand_name = fields.Char(string="Brand Name")
    is_under_warranty = fields.Boolean(string="Is Under Warranty?")

    product_origin = fields.Selection([
        ('egypt', 'Egypt'),
        ('china', 'China'),
        ('germany', 'Germany'),
        ('usa', 'USA'),
        ('other', 'Other'),
    ], string="Product Origin")
    technical_description = fields.Text(string="Technical Description")

    @api.constrains('warranty_period', 'is_under_warranty')
    def _check_warranty_period(self):
        for record in self:
            if record.warranty_period < 0:
                raise ValidationError(
                    "Warranty period cannot be negative."
                )

            if record.is_under_warranty and record.warranty_period <= 0:
                raise ValidationError(
                    "Warranty period must be greater than zero if the product is under warranty."
                )

            if not record.is_under_warranty and record.warranty_period != 0:
                raise ValidationError(
                    "Warranty period should be zero if the product is not under warranty."
                )

    # task 2
    #  Add new fields for pricing analysis to the product template model

    profit_margin = fields.Float(
        string="Profit Margin(%)", required=True, default=0.0, help="Profit margin percentage for the product.")

    expected_selling_price = fields.Monetary(
        string="Expected Selling Price", compute="_compute_expected_selling_price", currency_field="currency_id", store=True)
    profit_amount = fields.Monetary(
        string="Profit Amount", compute="_compute_profit_amount", currency_field="currency_id", store=True)

    @api.constrains('profit_amount')
    def _check_profit_amount(self):
        for record in self:
            if record.profit_amount < 0:
                raise ValidationError(
                    "Profit amount cannot be negative. Please check the profit margin and expected selling price."
                )

    @api.depends('standard_price', 'profit_margin')
    def _compute_expected_selling_price(self):
        for record in self:
            record.expected_selling_price = (
                record.standard_price +
                (record.standard_price * record.profit_margin / 100)
            )

    @api.depends('standard_price', 'expected_selling_price')
    def _compute_profit_amount(self):
        for record in self:
            record.profit_amount = (
                record.expected_selling_price - record.standard_price
            )
