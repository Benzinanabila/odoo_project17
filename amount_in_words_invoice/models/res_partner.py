from odoo import fields, models



class ResPartner(models.Model):
    """ Inherit the Purchase Order model to add amount in words in purchase
        order.Methods:_compute_number_to_words(self):
        Function to Change the purchase order total amount to words."""
    _inherit = 'res.partner'

    nif = fields.Char(string='N.I.F')
    nis = fields.Char(string='N.I.S')
    rc = fields.Char(string='R.C')
