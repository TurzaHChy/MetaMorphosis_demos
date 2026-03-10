from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    arrival = fields.Date(string="Arrival")
    commission = fields.Float(string="Commission", digits=(5, 2))