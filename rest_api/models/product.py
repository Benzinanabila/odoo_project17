from odoo import fields, models



class ProductTemplate(models.Model):
    #_name = 'product.modifying'
    _inherit = 'product.template'
    processor = fields.Char(string="computer Processor")
