from odoo import fields, models

from odoo17.odoo import api


class AccountMove(models.Model):
    """Inherit the Account Move to add amount in words in account move.
        Methods:_compute_number_to_words(self):
        Function to convert the invoice subtotal amount to words."""
    _inherit = 'account.move'
    partner_id = fields.Many2one(comodel_name= 'res.partner', string='partner Reference')

    number_to_words = fields.Char(string="Amount in Words (Total) : ",
                                  compute='_compute_number_to_words',
                                  help="To showing total amount in words")

    nif = fields.Char(related='partner_id.nif', string='N.I.F')
    nis = fields.Char(related='partner_id.nis', string='N.I.S')
    rc = fields.Char(related='partner_id.rc', string='R.C')
    def _compute_number_to_words(self):
        """Compute the amount to words in Invoice"""
        for rec in self:
            rec.number_to_words = rec.currency_id.amount_to_text(
                rec.amount_total)

