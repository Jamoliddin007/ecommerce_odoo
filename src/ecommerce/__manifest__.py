{
    'name': "ECommerce",
    'summary': "ECommerce moduli",
    'description': "Mahsulotlar, Toifalar, Buyurtmalar",
    'author': "Jamoliddin Saydirasulov UIC Group",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/menu.xml',
        'views/category_views.xml',
        'views/product_views.xml',
        'views/customer_views.xml',
        'views/order_views.xml',
        'views/order_line_views.xml',
    ],

    'installable': True,
    'application': True,
}
