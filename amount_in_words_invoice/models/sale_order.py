
from odoo import fields, models


class SaleOrder(models.Model):
    """
        Inherited the Sale Order model to add amount in words on sale order
        form view.Methods:_compute_number_to_words(self):
        Function to convert the sale order subtotal amount to words.
    """
    _inherit = 'sale.order'

    number_to_words = fields.Char(string="Amount in Words (Total) :",
                                  compute='_compute_number_to_words',
                                  help="To showing total amount in words")

    def _compute_number_to_words(self):
        """Compute the amount to words in Sale Order"""
        for rec in self:
            rec.number_to_words = rec.currency_id.amount_to_text(
                rec.amount_total)
