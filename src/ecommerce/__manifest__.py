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
        'views/menu.xml',
        'views/category_views.xml',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
}
