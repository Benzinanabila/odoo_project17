{
    'name': " Hospital Management System ",
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': """hospital""",
    'description': """ Hospital Management System""",
    'author': 'Ingénieurie des systèmes information',
    'company': 'Ingénieurie des systèmes information',
    'maintainer': 'Ingénieurie des systèmes information',
    'website': "https://www.cybrosys.com",
    'depends': ['mail', 'product', 'base'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'data/sequence.xml',
        'data/send_mail_appointement_template.xml',

        'wizard/custum_patient_wizard.xml',
        'wizard/cancel_appointement.xml',

        'views/patient.xml',
        'views/appointement_view.xml',
        'views/appointement_view_line.xml',
        'views/patient_readonly_view.xml',
        'views/patient_tag.xml',
        'views/menu.xml',

        'report/appointement_report.xml',
        'report/patient_report.xml',


    ],
    'assets':{
        'web.assets_backend':[

        ],

    'web.report_assets_common': [
        '/om_hospital/static/src/css/fonts.css',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

