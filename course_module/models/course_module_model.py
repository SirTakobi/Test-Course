#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import float_is_zero


class CourseModuleModel (models.Model):
    _name = 'course_module.model'
    _description = "Model for Course Module"

    name = fields.Char(
        required=True,
    )
    value = fields.Float(
        required=True,
    )

    def _sync_name_with_value(self):
        for record in self:
            record.name = str(record.value)

    @api.onchange(
        'value',
    )
    def onchange_value(self):
        self.ensure_one()
        self._sync_name_with_value()

    def multiply_float(self, value):
        for record in self:
            record.value *= value
        self._sync_name_with_value()

    def divide_float(self, value):
        if float_is_zero(value, precision_digits=2):
            raise UserError(_("Cannot divide by zero"))
        for record in self:
            record.value /= value
        self._sync_name_with_value()
