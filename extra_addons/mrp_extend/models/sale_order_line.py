from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    technical_drawing_ids = fields.One2many('drawing.technical', 'order_line_id', string='Drawing technical')

    def action_create_drawing_technical(self):
        return {
            'name': 'Create Technical Drawing',
            'type': 'ir.actions.act_window',
            'res_model': 'drawing.technical',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_order_line_id': self.id,
            },
        }