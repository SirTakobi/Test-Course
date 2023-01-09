#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import json

from addons.website.tools import MockRequest
from odoo import tests
from odoo.addons.course_module.tests.common import create_records
from odoo.addons.course_module.controllers.main import MainController


@tests.tagged('controllers', 'post_install', '-at_install')
class TestControllers (tests.HttpCase):

    def setUp(self):
        super().setUp()
        self.records = create_records(self.env, range(-10, 10))

    def test_get_all(self):
        self.authenticate('admin', 'admin')
        result = self.url_open('/course_module/get_all')
        content = result.text
        self.assertEqual(list(range(-10, 10)), json.loads(content))

    def test_greater(self):
        self.authenticate('admin', 'admin')
        result = self.url_open('/course_module/get_greater')
        content = result.text
        self.assertEqual(list(range(1, 10)), json.loads(content))

    def test_greater_than(self):
        self.authenticate('admin', 'admin')
        result = self.url_open('/course_module/get_greater/5')
        content = result.text
        self.assertEqual(list(range(6, 10)), json.loads(content))


@tests.tagged('controllers', 'post_install', '-at_install')
class TestControllersMockRequest (tests.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.records = create_records(cls.env, range(-10, 10))
        cls.controller = MainController()

    def test_get_all(self):
        with MockRequest(self.env):
            result = self.controller.get_all()
            content = result.response[0]
            self.assertEqual(list(range(-10, 10)), json.loads(content))
