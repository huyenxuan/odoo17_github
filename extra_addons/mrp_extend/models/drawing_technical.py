from odoo import models, fields

class DrawingTechnical(models.Model):
    _name = 'drawing.technical'
    _description = 'Drawing Technical'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Drawing Name', required=True, tracking=1)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=1)
    order_line_id = fields.Many2many('sale.order.line', string='Sale Order Line', tracking=1)
    attachment = fields.Binary(string='Attachment', attachment=True, tracking=1)
    attachment_filename = fields.Char(string='Attachment Filename', tracking=1)
    description = fields.Text(string='Description')
    date_created = fields.Date(string='Created Date', default=fields.Date.today)
