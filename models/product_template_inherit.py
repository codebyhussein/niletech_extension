
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    
    # Add new fields to the product template model
    
    warranty_period = fields.Integer(string="Warranty Period (in months)")
    brand_name = fields.Char(string="Brand Name")
    is_under_warranty = fields.Boolean(string="Is Under Warranty?")
    
    product_origin = fields.Selection([
       ('egypt','Egypt'),
       ('china','China'),
        ('germany','Germany'),
        ('usa','USA'),
        ('other','Other'),
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