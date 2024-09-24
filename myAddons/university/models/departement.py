




from odoo import models, fields, api
class UniversityDepartement(models.Model):
    _name= 'university.departement'
    _description = 'University Departement'
    name = fields.Char('name')
    code = fields.Char('code')

    professor_ids = fields.One2many(comodel_name='university.professor', inverse_name='departement_id')
    subject_ids = fields.One2many(comodel_name='university.subject', inverse_name='departement_id')
