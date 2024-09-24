


from odoo import models, fields, api
class UniversitySubject(models.Model):
    _name= 'university.subject'
    _description = 'University Subject'
    name = fields.Char('name')
    code = fields.Char('code')
    coeff = fields.Integer('Coefficient')

    departement_id = fields.Many2one(comodel_name='university.departement')

    professor_ids = fields.Many2many(comodel_name='university.professor',
                                     relation='sub_prof_rel',
                                     column1='name',
                                     column2='f_name')

