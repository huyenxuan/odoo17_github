from odoo import models, _, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.constrains('move_raw_ids')
    def _check_quantity(self):
        """Chức năng kiểm tra xem số lượng trong kho còn đủ để sản xuất hay không"""
        for rec in self:
            for line in rec.move_raw_ids:
                if line.quantity > line.product_id.qty_available:
                    subtraction = line.quantity - line.product_id.qty_available
                    raise UserError(_(f"Materials '{line.product_id.display_name}' are missing.\n"
                                      f"Quantity is still in the warehouse: {line.product_id.qty_available}.\n"
                                      f"Quantity needed: {line.quantity}.\n"
                                      f"Missing: {subtraction}"))
