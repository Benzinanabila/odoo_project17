


from odoo import models, fields, api
class UniversityClassroom(models.Model):
    _name= 'university.classroom'
    _description = 'University Classroom'
    _rec_name='classroom_name'
    _inherit= 'mail.thread'

    classroom_name = fields.Char(string='name')
    code = fields.Char('code')

    student_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')

    professor_ids = fields.Many2many(comodel_name='university.professor',
                                     relation='class_prof_rel',
                                     column1='name',
                                     column2='f_name')

    subject_ids = fields.Many2many(comodel_name='university.subject',
                                     relation='class_sub_rel',
                                     column1='classroom_name',
                                     column2='name',
                                    )

    num_prof = fields.Integer(string="Number of professors", compute='comp_prof')
    num_sub = fields.Integer(string="Number of subjects", compute='comp_sub')
    num_stu = fields.Integer(string="Number of students", compute='comp_stu')

    def comp_prof(self):
        self.num_prof= len(self.professor_ids)

    def comp_sub(self):
        self.num_sub= len(self.subject_ids)

    def comp_stu(self):
        self.num_stu= len(self.student_ids)

    @api.onchange('subject_ids')
    def chek_num_of_subject(self):
        if len(self.subject_ids) > 3:
            return {'warning': {'title': 'warning',
                                  'message': 'The number of subject must be less than 3'}}









