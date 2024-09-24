from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'
    _inherit= ['mail.thread']
    name = fields.Char(
        string=" Name" ,required=True ,tracking=True, translate=True
    )
    date_of_birth = fields.Date(string=" DOB" , tracking=True)
    age= fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection(
        [('male','Male'),('female','Female')], string="Gender", tracking=True
    )
    email = fields.Char(
        string="Email"
    )
    phone= fields.Char(string= "Phone number")
    tags_ids= fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="tags")
    image= fields.Image(string="Image")
#this def control us when we want to delete patient, it ensures that there is no appointemnt for this patient if there is not then delete if not it shows usererror
    @api.ondelete(at_uninstall=False)
    def _check_patient_appointement(self):
        for rec in self:
            domain= [('patient_id', '=', rec.id)]
            appointements = self.env['hospital.appointement'].search(domain)
            if appointements:
                raise UserError("you cannot delete the patient now." "\nAppointement existing for the patient: %s" % rec.name)

    @api.depends('date_of_birth')
    def _compute_age(self):

        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age= 0


