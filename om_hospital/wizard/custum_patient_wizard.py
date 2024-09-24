from odoo import models, fields, api
class CustumPatientWizard(models.TransientModel):
    _name= 'custum.patient.data.wiz'
    patient_id2= fields.Many2one('hospital.patient', 'patients')

    def button_confirm(self):
        context = self.env.context
        custum_patient_rec_id = context.get('custum_patient_data_rec_id', False)
        record = self.env['hospital.appointement'].browse(custum_patient_rec_id)
        record.patient_id2 = self.patient_id2.id
