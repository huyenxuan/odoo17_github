from odoo import models, fields

class DrawingTechnical(models.Model):
    _name = 'drawing.technical'
    _description = 'Drawing Technical'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Drawing Name', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    attachment = fields.Binary(string='Attachment', attachment=True)
    attachment_filename = fields.Char(string='Attachment Filename')
    description = fields.Text(string='Description')
    date_created = fields.Date(string='Created Date', default=fields.Date.today)
