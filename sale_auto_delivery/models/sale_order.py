from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        # Auto-validate delivery orders
        for order in self:
            pickings = order.picking_ids.filtered(lambda p: p.state in ['draft', 'confirmed', 'assigned'])
            for picking in pickings:
                # Confirm picking if it's draft
                if picking.state == 'draft':
                    picking.action_confirm()
                # Reserve stock
                picking.action_assign()   # <-- Correct method in Odoo 19
                # Validate delivery
                try:
                    picking.button_validate()
                except Exception as e:
                    _logger.warning(f"Could not auto-validate picking {picking.name}: {e}")

        return res