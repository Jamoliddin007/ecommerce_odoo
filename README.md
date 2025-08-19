# Ecommerce Odoo Module  

Modular and extensible **Ecommerce Management System** built with **Odoo 18**.  
Includes full support for products, categories, customers, orders, and access control.  

---

## 🚀 Features  

### Products & Categories  
- Manage products with category hierarchy  
- One2many / Many2one relational structure  

### Customers & Orders  
- Customer registration and order management  
- Order line handling with computed totals  

### Security & Access  
- Fine-grained access control via `ir.model.access.csv`  
- Role-based permissions for users  

### Sequences  
- Unique sequence generator for orders  

### Views  
- Intuitive XML forms, tree, and menu items  
- Easy navigation for end-users  

---

## 📂 Project Structure  

ecommerce_odoo/
├── conf/
│ └── odoo.conf # Odoo configuration file
└── src/
└── ecommerce/
├── manifest.py # Module manifest
├── models/ # Business logic
│ ├── customer.py
│ ├── order.py
│ ├── order_line.py
│ └── category.py
├── views/ # XML views
├── data/ # Initial data (sequences)
└── security/ # Access control rules


---

## ⚙️ Installation  

Clone repository:  
```bash
git clone https://github.com/<your-username>/ecommerce_odoo.git

