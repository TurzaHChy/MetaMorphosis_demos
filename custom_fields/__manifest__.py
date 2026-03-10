{
    'name': 'Custom Fields',
    'version': '1.0',
    'summary': 'Add arrival date field in sales order line',
    'author': 'Turza',
    'depends': ['sale'],
    'data': [
        'views/sale_order_line_views.xml',
        'views/sale_report.xml',
    ],
    'installable': True,
    'application': False,
}