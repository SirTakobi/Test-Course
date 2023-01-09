#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import json

from odoo import http
from odoo.http import request


class MainController (http.Controller):

    def _get_records_values(self, domain=None):
        if domain is None:
            domain = list()
        record_model = request.env['course_module.model']
        records = record_model.search(domain)
        records_values = sorted(records.mapped('value'))
        return records_values

    @http.route(
        route='/course_module/get_all',
        type='http',
    )
    def get_all(self):
        records_values = self._get_records_values()
        return json.dumps(records_values)

    @http.route(
        route=[
            '/course_module/get_greater/<int:value>',
            '/course_module/get_greater',
        ],
        type='http',
    )
    def get_greater(self, value=None):
        if value is None:
            value = 0
        records_values = self._get_records_values(
            domain=[
                ('value', '>', value),
            ],
        )
        return json.dumps(records_values)
