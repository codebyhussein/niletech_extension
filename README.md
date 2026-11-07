# Niletech Custom Module

This module is a custom Odoo development project created to extend business functionality in a clean, maintainable, and reusable way. It is designed not only for product management, but also to support future customizations in other Odoo areas such as Inventory, Sales, Purchase, Accounting, or HR.

The project demonstrates how custom logic, validation rules, computed fields, and UI customizations can be added to Odoo without breaking the standard behavior of the base application.

## Project goal

The main goal of this module is to improve business processes by adding custom data, automated calculations, and validation rules to standard Odoo records.

This module can be extended in the future to support:

- Inventory custom fields and stock controls
- Sales and pricing logic
- Purchase order tracking
- Accounting and financial reporting
- HR and employee-related data
- Warehouse or logistics customization

## Current scope

This module currently extends the Product form in two main tasks:

### Task 1: Technical product information

This task adds fields for product technical and warranty information.

#### Included fields

- Brand Name
- Product Origin
- Warranty Period
- Is Under Warranty
- Technical Description

#### Validation rules

- Warranty period cannot be negative.
- If the product is under warranty, the warranty period must be greater than zero.
- If the product is not under warranty, warranty period must be zero.

#### Purpose

This helps the business maintain more complete product records and ensure consistency in product technical details.

### Task 2: Pricing analysis

This task adds logic for product pricing and profitability analysis.

#### Included fields

- Profit Margin (%)
- Expected Selling Price
- Profit Amount

#### Calculation logic

- Expected Selling Price = Standard Price + (Standard Price x Profit Margin / 100)
- Profit Amount = Expected Selling Price - Standard Price

#### Validation rules

- Profit amount cannot be negative.

#### Purpose

This allows users to analyze pricing strategy and ensure that the product margin remains valid and realistic.

## Future-ready design

The module follows a standard Odoo customization structure that can be reused for other modules. The same pattern can be applied to other models when creating additional customizations.

Typical future customizations may include:

- Adding new fields to stock.picking or product.product
- Creating computed values in inventory or sales records
- Adding business validations to existing models
- Customizing views to show important information in tabs or sections
- Writing logic to automate workflows based on business rules

## Module structure

- models/product_template_inherit.py
  - custom fields
  - constraints
  - computed methods
  - business logic

- views/product_template_inherit_view.xml
  - custom view inheritance
  - tabs and form layout

- __manifest__.py
  - module metadata
  - dependencies
  - data files

## How this module works

The module inherits the standard Odoo product model and adds extra fields directly to the Product form. These custom fields are visible in dedicated tabs and are validated through Odoo constraints.

This keeps the original Odoo functionality intact while adding company-specific features needed for business operations.

## Installation

1. Copy the module folder into your Odoo custom addons directory.
2. Update the addons list in Odoo.
3. Install the module from the Apps menu.
4. Open a product record and review the new sections in the form.

## Notes for developers

This project is a good example of how to create custom Odoo modules in a clean, readable, and maintainable way.

Best practices used here:

- model inheritance instead of modifying core data directly
- constraint validation for business rules
- computed fields for automated values
- view inheritance for UI customization
- code organized by task and purpose

## Summary

This module is a foundation for custom Odoo enhancement work. It is currently focused on product-related fields, but it is intentionally structured so that future customizations can be added to other modules as needed.

Its purpose is simple: make Odoo more useful for real business needs while keeping the code organized, readable, and easy to extend.
