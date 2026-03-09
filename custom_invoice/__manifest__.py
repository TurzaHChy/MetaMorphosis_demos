{
    'name': 'Custom Invoice',
    'version': '19.0.1.0',
    'summary': 'Simple custom invoice module',
    'category': 'Accounting',
    'author': 'Turza',
    'depends': ['base','account','account_edi_ubl_cii',],
    'data': [
    'report/bill_invoice_template.xml',
    # 'views/invoice_views.xml',
],
    'installable': True,
    'application': True,
}