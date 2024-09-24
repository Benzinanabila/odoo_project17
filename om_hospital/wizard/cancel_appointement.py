import datetime

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
class CancelAppointementWizard(models.TransientModel):
    _name= 'cancel.appointement.data.wiz'
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointementWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointement_id'] = self.env.context.get('active_id')
        return res

    # , ('priority', 'in', ('0', '1', False))]
    appointement_id = fields.Many2one('hospital.appointement', string="Appointement", domain=[('state', '=', 'draft')])
    reason= fields.Text(string="Reason")
    date_cancel= fields.Date(string="cancellation date")

    def action_cancel(self):
        if self.appointement_id.date == fields.Date.today():
            raise ValidationError(_("Sorry, cancellation is not allowed on the same day of booking!"))
        self.appointement_id.state = 'cancel'
        return