from odoo import models, fields
from num2words import num2words

class AccountMove(models.Model):
    _inherit = 'account.move'

    employee_id = fields.Many2one('hr.employee', string='Salesman')
    delivered_by = fields.Many2one('hr.employee', string='Delivered By')
    receipt_note = fields.Text(string='Receipt Note')

    def number_to_words(self, amount):
        try:
            return num2words(amount, lang='en').capitalize()
        except Exception:
            return str(amount)

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    additional_discount = fields.Float(string='Additional Discount')
    vendor_id = fields.Many2one('res.partner', string='Vendor', domain=[('supplier_rank', '>', 0)])
