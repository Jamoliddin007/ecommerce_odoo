from odoo import models, fields, api
from datetime import date


class Order(models.Model):
    _name = "ecommerce.order"
    _description = "Buyurtma"
    _order = "id desc"

    # Buyurtma raqami
    name = fields.Char(
        string="Buyurtma raqami",
        required=True,
        copy=False,
        readonly=True,
        default="Yangi",
    )

    # Mijoz
    customer_id = fields.Many2one(
        "ecommerce.customer",
        string="Mijoz",
        required=True,
    )

    # Yetkazib berish muddati
    deadline = fields.Date(
        string="Qachongacha yetkazib berish kerak"
    )

    # Qolgan kunlar
    days_left = fields.Integer(
        string="Qancha muddat qoldi (kun)",
        compute="_compute_days_left",
        store=True,
    )

    # Buyurtmadagi mahsulotlar soni
    product_count = fields.Integer(
        string="Mahsulotlar soni",
        compute="_compute_product_count",
        store=True,
    )

    # Buyurtma qatorlari
    order_line_ids = fields.One2many(
        "ecommerce.order.line",
        "order_id",
        string="Buyurtma qatorlari",
    )

    # Name ko‘rinishi
    def name_get(self):
        result = []
        for order in self:
            display_name = f"{order.name} - {order.customer_id.full_name}"
            result.append((order.id, display_name))
        return result

    # Sequence orqali name yaratish
    @api.model
    def create(self, vals):
        if vals.get("name", "Yangi") == "Yangi":
            vals["name"] = self.env["ir.sequence"].next_by_code("ecommerce.order") or "Yangi"
        return super().create(vals)

    # Qolgan kunlarni hisoblash
    @api.depends("deadline")
    def _compute_days_left(self):
        today = date.today()
        for record in self:
            if record.deadline:
                record.days_left = (record.deadline - today).days
            else:
                record.days_left = 0

    # Mahsulotlar sonini hisoblash
    @api.depends("order_line_ids")
    def _compute_product_count(self):
        for record in self:
            record.product_count = sum(line.quantity for line in record.order_line_ids)
