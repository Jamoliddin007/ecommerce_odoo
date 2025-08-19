Ecommerce Odoo Module

Modular and extensible Ecommerce Management System built with Odoo 18.
Includes full support for products, categories, customers, orders, and access control.

🚀 Features

Products & Categories

Manage products with category hierarchy

One2many / Many2one relational structure

Customers & Orders

Customer registration and order management

Order line handling with computed totals

Security & Access

Fine-grained access control via ir.model.access.csv

Role-based permissions for users

Sequences

Unique sequence generator for orders

Views

Intuitive XML forms, tree, and menu items

Easy navigation for end-users

## 📂 Project Structure



⚙️ Installation

Clone repository:

git clone https://github.com/<your-username>/ecommerce_odoo.git


Add module path to your odoo.conf:

addons_path = /path/to/ecommerce_odoo/src


Update and install module:

python odoo/odoo-bin -c conf/odoo.conf -u ecommerce

🧪 Usage

Go to Ecommerce → Products to manage products.

Go to Ecommerce → Orders to create and manage customer orders.

Sequences auto-generate unique order references.

Role-based access ensures proper security for users.

🔒 Security

Access rights defined in security/ir.model.access.csv.

Supports roles: Manager, User, Guest.

📖 Tech Stack

Odoo 18

PostgreSQL

Python 3.10+

XML for views & data

📈 Roadmap

 Add reporting & analytics dashboards

 Integrate payment gateways

 Multi-currency support

 REST API for external integration

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

👤 Author

Jamoliddin

Software Engineer | Odoo Specialist | Python & Django Developer

GitHub# ecommerce_odoo
