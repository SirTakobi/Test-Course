#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': "Course Module",
    'version': '12.0.1.0.0',
    'author': "TAKOBI",
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course_module_model_views.xml',
        'views/course_module_wizard_views.xml',
        'views/templates.xml',
    ],
}
