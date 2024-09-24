
{
    'name': "Amount In Words In Invoice, Sale Order And Purchase Order",
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': """Showing the subtotal amounts of invoice, sale order 
     and purchase order in words""",
    'description': """The Module to Shows The Subtotal Amount in Words 
     on Invoice, Sale Order and Purchase Order""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['sale_management', 'account', 'purchase','base'],

    'data': [
        'data/account_move_data.xml',
        'data/purchase_order_data.xml',
        'data/sale_order_data.xml',
        'views/account_move_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/res_partner_views.xml',
        'report/account_move_reports.xml'


    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
