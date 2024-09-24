from odoo import fields, models



class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient tag'
    _order= 'sequence,id'
    name = fields.Char(
        string=" Name" ,required=True
    )
    color= fields.Integer(string="color")
    color_2= fields.Integer(string="color 2")
    active= fields.Boolean(string="Active", default= True)
    sequence= fields.Integer(default=10)

    _sql_constraints = [('tag_name_unique', 'unique(name, active)', 'tag name already exists'),
                        ('check_sequence', 'check(sequence >0)', 'sequence must be no zero positive number')]
