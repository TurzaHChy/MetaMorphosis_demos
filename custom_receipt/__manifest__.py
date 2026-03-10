{
    'name': 'Custom Receipt',
    'version': '1.0',
    'summary': 'Customized Invoice Layout for EDI and Standard Reports',
    'category': 'Accounting',
    'author': 'Turza',
    'depends': [
        'base',
        'account',
        'account_edi_ubl_cii',  
        'sale',                 
        'hr',
        'sale_stock',
    ],
    'data': [
        'views/receipt_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}