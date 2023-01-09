#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import UserError


class CourseModuleWizard (models.TransientModel):
    _name = 'course_module.wizard'
    _description = "Wizard for Course Module"

    action = fields.Selection(
        selection=[
            ('div', "Divide"),
            ('mul', "Multiply"),
            ('mul10', "Multiply by 10"),
        ],
        required=True,
    )
    value = fields.Float()

    def _get_selected_records(self):
        record_model = self.env.context.get('active_model')
        record_ids = self.env.context.get('active_ids')
        records = self.env[record_model].browse(record_ids)
        return records

    def do_action(self):
        self.ensure_one()
        records = self._get_selected_records()

        action = self.action
        value = self.value
        if action == 'mul':
            records.multiply_float(value)
        elif action == 'div':
            records.divide_float(value)
        elif action == 'mul10':
            records.multiply_float(10)
        else:
            raise UserError(
                _("Action {action} not managed")
                .format(
                    action=action,
                )
            )
