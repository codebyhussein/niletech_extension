# NileTech Trading

NileTech Trading is a custom Odoo module that extends product and sales order forms with additional business information, pricing calculations, and delivery controls.

The module uses Odoo model and view inheritance, adding project-specific functionality while leaving the standard Odoo source code unchanged.

## Features

| Task | Area | What it adds |
|---|---|---|
| 1. Technical product information | Product form | Product brand, origin, warranty, and technical description |
| 2. Pricing analysis | Product form | Profit margin, computed selling price, and computed profit |
| 3. Delivery information | Sales Order form | Customer PO, delivery date and priority, installation, and delivery instructions |

## Screenshots

### Product pricing analysis

The product form shows the cost, profit margin, computed expected selling price, and computed profit amount.

![Product form showing pricing analysis](static/description/product_form.png)

### Sales order delivery information

The Sales Order form includes a Delivery Information tab for capturing delivery requirements.

![Sales Order form showing delivery information](static/description/sales_order_delivery.png)

## Task Details

### Task 1: Technical Product Information

Adds a **Technical Information** tab to the Product form with:

- Brand Name
- Product Origin
- Warranty Period (in months)
- Is Under Warranty?
- Technical Description

The warranty validation rules ensure that the period is not negative, is greater than zero when the product is under warranty, and is zero when it is not under warranty. The warranty period field is shown only when the product is marked as under warranty.

### Task 2: Pricing Analysis

Adds a **Pricing Analysis** tab to the Product form with:

- Cost (standard price)
- Profit Margin (%)
- Expected Selling Price
- Profit Amount

The expected selling price and profit amount are computed and stored:

- **Expected Selling Price** = Cost + (Cost × Profit Margin / 100)
- **Profit Amount** = Expected Selling Price − Cost

The module rejects a negative profit amount.

### Task 3: Delivery Information

Adds a **Delivery Information** tab to the Sales Order form with:

- Customer Purchase Order
- Expected Delivery Date
- Delivery Priority (Normal, Urgent, or Very Urgent)
- Requires Installation?
- Special Delivery Instructions

The expected delivery date cannot be earlier than the order date. An expected delivery date is also required before a quotation or sales order can be confirmed.

## Module Structure

```text
niletech_product_extension/
├── models/
│   ├── product_template_inherit.py
│   └── sale_order_inherit.py
├── views/
│   ├── product_template_inherit_view.xml
│   └── sale_order_inherit_view.xml
├── static/
│   └── description/
│       ├── product_form.png
│       └── sales_order_delivery.png
├── __manifest__.py
└── README.md
```

## Requirements

- Odoo 17
- Odoo modules: `product` and `sale_management` (along with Odoo's `base` module)

## Installation

1. Copy `niletech_product_extension` into an Odoo custom addons directory.
2. Ensure the custom addons directory is included in Odoo's `addons_path`.
3. Restart the Odoo server.
4. Update the Apps list and install **NileTech Trading**.

## Usage

- Open a product to maintain its technical information and review pricing calculations.
- Open a quotation or sales order and use the **Delivery Information** tab to enter delivery details.
- Set an expected delivery date before confirming the quotation or order.

## Development Notes

- Custom fields and business rules are defined in `models/`.
- Form changes use inherited views in `views/`.
- The screenshots are stored in `static/description/` and are referenced relative to this README.
- Update the module after changing its Python or XML files.
