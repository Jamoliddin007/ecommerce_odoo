from odoo import models, fields, api

class Category(models.Model):
    _name = "ecommerce.category"
    _description = "Kategoriyalar"

    name = fields.Char(string="Nomi", required=True)
    product_ids = fields.One2many(comodel_name="ecommerce.product", inverse_name="category_id", string="Mahsulotlar")
    product_count = fields.Integer(string="Mahsulotlar soni", compute="_compute_product_count",store=True)

    @api.depends("product_ids")
    def _compute_product_count(self):
        for record in self:
            record.product_count = len(record.product_ids)

