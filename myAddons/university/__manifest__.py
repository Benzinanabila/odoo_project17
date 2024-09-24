# -*- coding: utf-8 -*-
{
    'name': "university",

    'summary': "univ",

    'description': "university",
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',
    'installable': True,
    'application': True,
    'sequence': -100,
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','mail','website'],
    'assets': {
        'web.assets_backend': [
            'university/static/src/css/fonts.css',
        ],
    },
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/studentLine.xml',
        'views/classroom_views.xml',
        'views/professor_views.xml',
        'views/subject_views.xml',
        'views/departement_views.xml',
        'views/university_template.xml',
        'data/mail_template.xml',
        'report/student_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [],
}

