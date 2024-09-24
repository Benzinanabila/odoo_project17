from odoo import fields, models,api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date


class Appointement(models.Model):
    _name = 'hospital.appointement'
    _description = 'hospital appointement'
    _inherit= ['mail.thread']
    _rec_names_search=['reference','patient_id']
    _rec_name= 'patient_id'
    name= fields.Char(string="name")
    reference= fields.Char(string="reference", copy=False, required=True, default="new", readonly=True)
    patient_id = fields.Many2one('hospital.patient', string="Patients", required=False, Ondelete='cascade')
    patient_id2 = fields.Many2one('hospital.patient', 'related patients', readonly=True)
    # ondelete='restrict' ondelete='set null'
    date = fields.Date(string=" Date")
    note = fields.Text(string=" Note")
    state= fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('engoing','Engoing'),('done','Done'),('cancel','Cancel')], default='draft', Tracking=True)
    #create relation between appointement and appointementLine
    appointement_line_ids= fields.One2many('hospital.appointement.line', 'appointement_id', string="lines")
    total_qty=fields.Float(compute='_compute_total_qty', string="total quantity", store= True)
    date_of_birth = fields.Date(related='patient_id.date_of_birth', store= True, groups="om_hospital.group_hospital_doctors")
    my_currency_id = fields.Many2one("res.currency", string="(currency)", help="Please select the currency")
    Prix = fields.Monetary("Prix", currency_field= "my_currency_id")
    #create def to can duplicate appointements
    def copy(self, default=None):
        default= dict(default or {})
        copied_count = self.env['hospital.appointement'].search_count([('name', '=like', f"Copy of {self.name}%")])
        if not copied_count:
            new_name= f"Copy of {self.name}"
        else:
            new_name= f"Copy of {self.name} ({copied_count})"
        default.update({'name': new_name})
        return super().copy(default=default)

#to get total_qty on appointement_report
    def get_total_qty(self):
        total_qty=0
        for appointement in self.appointement_line_ids:
            total_qty+= appointement.qty
        return total_qty
    #incrementer reference it's depends to sequence.xml
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference']=="new":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointement')
        return super().create(vals_list)
    #get total_qty on appointement view
    @api.depends('appointement_line_ids','appointement_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointement_line_ids.mapped('qty'))
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.reference}] {rec.patient_id.name}"

    # action_confirm  action_ongoing action_done action_cancel those def for button that control statusbar(state)
    def action_confirm(self):
        for rec in self:
            rec.state= 'confirmed'
    def action_ongoing(self):
        for rec in self:
            rec.state= 'engoing'

    def action_done(self):
        for rec in self:
            rec.state= 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Done',
                'type': 'rainbow_man',
            }
        }
    def action_cancel(self):
        action = self.env.ref('om_hospital.action_hospital_cancel').read()[0]
        return action
        # return {
        #     'name': 'Select appointement',
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'cancel.appointement.data.wiz',
        #     'target': 'new',
        #     'context': {}
        # }
    def action_share_whatsapp(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Missing phone number in patient record"))
        message= 'Hi %s, your appointement number is:%s, Thank u' %(self.patient_id.name, self.reference)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.patient_id.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target' : 'new',
            'url': whatsapp_api_url
        }

    def action_send_mail(self):

        template_id= self.env.ref('om_hospital.appointement_mail_template')
        for rec in self:
            # email_values= {'subject': 'appointement details'  {{object.reference}}}
            template_id.send_mail(rec.id)

    def open_wizard(self):
        return {
            'name' : 'Select patient',
            'type' : 'ir.actions.act_window',
            'view_mode' : 'form',
            'res_model' : 'custum.patient.data.wiz',
            'target' : 'new',
            'context' : {'custum_patient_data_rec_id' : self.id}
        }
class AppointementLine(models.Model):
    _name = 'hospital.appointement.line'
    _description = 'hospital appointement line'
    appointement_id=fields.Many2one('hospital.appointement', string="Appointement")
    product_id = fields.Many2one('product.product', string="Product", required=True)
    qty= fields.Float(string="Quantity")
