from odoo import  models, fields, api

class Product(models.Model):
    _name = "ecommerce.product"
    _description = "Product"

    name = fields.Char(string="Name", required=True)
    slug = fields.Char(string="Slug", compute="_compute_slug", store=True)
    category_id = fields.Many2one(
        "ecommerce.category",
        string="Kategoriyasi",
        ondelete="set null"
    )
    has_category = fields.Boolean(
        string="Biror kategoriyaga tegishlimi?",
        compute="_compute_has_category",
        store=True
    )
    sale_price = fields.Float(string="Sotuv narxi")
    cost_price = fields.Float(string="Tannarxi")
    profit_percent = fields.Float(
        string="Mahsulot ustiga necha foiz qo'yilgan",
        compute="_compute_profit_percent",
        store=True
    )
    length = fields.Float(string="Bo'yi")
    width = fields.Float(string="Eni")
    height = fields.Float(string="Balandligi")
    volume = fields.Float(
        string="Hajmi",
        compute="_compute_volume",
        store=True
    )
    @api.depends('name')
    def _compute_slug(self):
        for record in self:
            if record.name:
                record.slug = record.name.lower().replace(" ","-")
            else:
                ""

    @api.depends('category_id')
    def _compute_has_category(self):
        for record in self:
            record.has_category = bool(record.category_id)

    @api.depends('sale_price', 'cost_price')
    def _compute_profit_percent(self):
        for record in self:
            if record.cost_price > 0:
                record.profit_percent = ((record.sale_price - record.cost_price) / record.cost_price) * 100
            else:
                record.profit_percent = 0.0

    @api.depends('length', 'width', 'height')
    def _compute_volume(self):
        for record in self:
            if record.height and record.width and record.length:
                record.volume = record.length * record.height * record.width
            else:
                record.volume = 0.0

    

