from odoo import models, fields, api
from datetime import date

class Customer(models.Model):
    _name = "ecommerce.customer"
    _description = "Mijozlar"
    _rec_name = "full_name"

    first_name = fields.Char(string="Ismi", required=True)
    last_name = fields.Char(string="Familyasi", required=True)
    middle_name = fields.Char(string="Sharifi")
    birth_date = fields.Date(string="Tug'ilgan sanasi")
    email = fields.Char(string="Email manzili")
    country = fields.Char(string="Davlati")
    region = fields.Char(string="Viloyati")
    district = fields.Char(string="Tumani")
    street = fields.Char(string="Ko'chasi")

    full_name = fields.Char(
        string="To'liq ismi",
        compute="_compute_full_name",
        store=True
    )
    initials = fields.Char(
        string="Ism qisqartmasi",
        compute="_compute_initials",
        store=True
    )
    age_text = fields.Char(
        string="Yoshi",
        compute="_compute_age_text",
        store=True
    )
    email_domain = fields.Char(
        string="Email domeni",
        compute="_compute_email_domain",
        store=True
    )
    full_address = fields.Char(
        string="To‘liq manzili",
        compute="_compute_full_address",
        store=True
    )
    order_count = fields.Integer(
        string="Buyurtmalar soni",
        compute="_compute_order_count",
        store=True
    )

    orders = fields.One2many(
        'ecommerce.order',
        'customer_id',
        string="Buyurtmalari"
    )

    @api.depends('first_name', 'last_name', 'middle_name')
    def _compute_full_name(self):
        for record in self:
            parts = [record.first_name, record.last_name, record.middle_name]
            record.full_name = " ".join(word for word in parts if word)

    @api.depends('first_name', 'last_name', 'middle_name')
    def _compute_initials(self):
        for record in self:
            initials = "".join([
                record.first_name[0].upper() if record.first_name else '',
                record.last_name[0].upper() if record.last_name else '',
                record.middle_name[0].upper() if record.middle_name else '',
            ])
            record.initials = initials

    @api.depends('birth_date')
    def _compute_age_text(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                delta = today - record.birth_date
                years = delta.days // 365
                months = (delta.days % 365) // 30
                days = (delta.days % 365) % 30
                record.age_text = f"{years}yil {months}oy {days}kun"
            else:
                record.age_text = False

    @api.depends('email')
    def _compute_email_domain(self):
        for record in self:
            if record.email and '@' in record.email:
                record.email_domain = record.email.split('@')[-1]
            else:
                record.email_domain = False

    @api.depends('country', 'region', 'district', 'street')
    def _compute_full_address(self):
        for record in self:
            parts = [record.street, record.district, record.region, record.country]
            record.full_address = ", ".join(address for address in parts if address)

    @api.depends('orders')
    def _compute_order_count(self):
        for record in self:
            record.order_count = len(record.orders)

