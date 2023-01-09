#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import Form


def create_records(env, values):
    record_model = env['course_module.model']
    records = record_model.browse()
    for value in values:
        record_form = Form(record_model)
        record_form.value = value
        record = record_form.save()
        records |= record
    return records
