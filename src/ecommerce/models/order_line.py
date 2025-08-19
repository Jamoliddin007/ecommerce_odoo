from odoo import models, fields, api


class OrderLine(models.Model):
    _name = "ecommerce.order.line"
    _description = "Order Line"

    order_id = fields.Many2one(
        "ecommerce.order",
        string="Order",
        required=True,
        ondelete="cascade"
    )

    customer_id = fields.Many2one(
        "ecommerce.customer",
        string="Mijoz",
        related="order_id.customer_id",
        store=True,
        readonly=True
    )

    product_id = fields.Many2one(
        "ecommerce.product",
        string="Mahsulot",
        required=True
    )

    quantity = fields.Integer(string="Miqdori", default=1)
    price_unit = fields.Float(string="Sotilish narxi", required=True)
    tax_percent = fields.Float(string="Soliq (%)", default=0.0)
    discount_percent = fields.Float(string="Chegirma (%)", default=0.0)

    total_price = fields.Float(
        string="Umumiy narx",
        compute="_compute_total_price",
        store=True
    )

    profit_percent = fields.Float(
        string="Foyda (%)",
        compute="_compute_profit",
        store=True
    )

    profit_amount = fields.Float(
        string="Foyda (pulda)",
        compute="_compute_profit",
        store=True
    )

    @api.depends("quantity", "price_unit", "tax_percent", "discount_percent")
    def _compute_total_price(self):
        for record in self:
            subtotal = record.price_unit * record.quantity
            subtotal += subtotal * (record.tax_percent / 100)  # soliq
            subtotal -= subtotal * (record.discount_percent / 100)  # chegirma
            record.total_price = subtotal

    @api.depends("total_price", "quantity", "price_unit")
    def _compute_profit(self):
        for record in self:
            cost = record.price_unit * record.quantity
            profit = record.total_price - cost
            record.profit_amount = profit
            record.profit_percent = (profit / cost * 100) if cost else 0
