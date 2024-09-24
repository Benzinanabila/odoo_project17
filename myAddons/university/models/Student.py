# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pygments.lexer import default
from pygments.styles.dracula import selection

from odoo17.odoo.tools.safe_eval import datetime


class UniversityStudent(models.Model):
    _name= 'university.student'
    _description = 'University Student'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    sexe = fields.Selection([('male','male'),('female','female')])
    identity_card= fields.Char('Identity card')
    adress= fields.Text('Adress')
    birthday= fields.Date('birthday')
    registration_date = fields.Date('Registration date')
    email= fields.Char()
    phone= fields.Char()
    university= fields.Char()
    departement_id = fields.Many2one(comodel_name='university.departement')
    classroom_id = fields.Many2one(comodel_name='university.classroom')
    image = fields.Image(string="Image")
    subject_ids = fields.Many2many(related= 'classroom_id.subject_ids')
    date_of_today = fields.Datetime(string="date of today", default=fields.Datetime.now)
    student_subject_ids = fields.One2many('university.student.line', 'student_id', string='Subjects')

    level = fields.Selection([('L1', 'Level1'), ('L2', 'Level2'), ('L3', 'Level3'), ('finished', 'Finished')], default='L1', store=True)
    moyen = fields.Float(compute='_compute_moyen', string="Moyen", store=True)
    someCredit = fields.Integer(compute='_compute_credit', string="Crédit", store=True)
    ref_field_id = fields.Reference(selection=[('university.professor','Professor'),
                                               ('university.departement','departement'),
                                               ('university.subject','subject'),
                                               ('university.classroom','Classroom')], string="Reference", help="please select the reference")
    api.depends('classroom_id.classroom_name','f_name','l_name')
    def _compute_display_name(self):
        for student in self:
            student.display_name ='[' + student.classroom_id.classroom_name + ']' + ' ' + student.f_name + ' ' + student.l_name
    # @api.one
    @api.constrains('registration_date','birthday')
    def check_date(self):
        if self.birthday > self.registration_date:
            raise ValidationError('The birthday must be inferior than registration date')

    @api.depends('student_subject_ids', 'student_subject_ids.note')
    def _compute_moyen(self):
        for rec in self:
            note = rec.student_subject_ids.mapped('note')
            coef = rec.student_subject_ids.mapped('coef')
            if note and coef and len(note) == len(coef) and sum(coef)!= 0:
                # Calculer la somme des produits élément par élément entre note et coef
                total = sum(n * c for n, c in zip(note, coef))
                # Diviser par la somme des coefficients pour obtenir la moyenne pondérée
                rec.moyen =  round(total / sum(coef), 2)
            else:
                rec.moyen = 0.0


    @api.depends('student_subject_ids', 'student_subject_ids.note','student_subject_ids.credit')
    def _compute_credit(self):

        for rec in self:
            someCredit = 0
            note = rec.student_subject_ids.mapped('note')
            credit = rec.student_subject_ids.mapped('credit')

            for subject in rec.student_subject_ids:
                if subject.note >= 10:
                    someCredit += subject.credit

                # Assign the computed credit to the record
            rec.someCredit = someCredit
    def level2(self):
        for rec in self:
            rec.level= 'L2'

    def level3(self):
        for rec in self:
            rec.level= 'L3'
    def finished(self):
        for rec in self:
            rec.level= 'finished'





class UniversityStudentLine(models.Model):
    _name = 'university.student.line'
    _description = 'Student line'
    classroom_id = fields.Many2one(comodel_name='university.classroom')
    subject_ids = fields.Many2many(related='classroom_id.subject_ids')
    student_id = fields.Many2one('university.student', string="Student")
    subject_id = fields.Many2one('university.subject', string="Subject")
    note = fields.Float('Note')
    coef = fields.Integer(string="Coef", store=True)
    credit = fields.Integer(string="Crédit", store=True)

