from odoo import models, fields

from odoo import api
from pygments.lexer import default


class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _description = 'University Professor'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    sexe = fields.Selection([('male','male'),('female','female')])
    identity_card= fields.Char('Identity card')
    adress= fields.Text('Adress')
    birthday= fields.Date('birthday')
    inscription_date = fields.Date('date of inscription')
    email= fields.Char()
    phone= fields.Char()
    active= fields.Boolean(default=True)
    departement_id = fields.Many2one(comodel_name='university.departement')
    subject_id = fields.Many2one(comodel_name='university.subject')

    classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                     relation='prof_class_rel',
                                     column1='f_name',
                                     column2='name')

    professor_id = fields.Many2one('university.professor')
    @api.depends('departement_id','f_name','l_name')
    def _compute_display_name(self):
        for prof in self:
            if prof.departement_id and prof.departement_id.name:
                prof.display_name = f"{prof.departement_id.name} {prof.f_name} {prof.l_name}"
            else:
                prof.display_name = f"{prof.f_name} {prof.l_name}"

    def action_send_mail(self):

        template_id= self.env.ref('university.email_template_prof')
        for rec in self:
            #email_values= {'subject': 'test on'}
            template_id.send_mail(rec.id, force_send=True)




    def get_date(self):
        date = fields.Date.today()
        return date
    date = fields.Date(string='Date', default= get_date)
