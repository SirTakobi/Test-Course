#  Copyright 2023 Simone Rubino - TAKOBI
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import tests
from odoo.addons.course_module.tests.common import create_records
from odoo.exceptions import UserError
from odoo.fields import first
from odoo.tests import Form


class TestModelSavepoint (tests.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.records = create_records(cls.env, range(1, 5000))

    def test_onchange_value(self):
        """The name of the record is the string representation of its value."""
        record = first(self.records)
        value = 2.0

        record.value = value
        # Onchanges are only triggered when using Form
        self.assertNotEqual(record.name, str(value))

        record_form = Form(record)
        record_form.value = value
        record = record_form.save()

        self.assertEqual(record.name, str(value))

    def test_multiplication(self):
        """Multiplication works correctly."""
        record = first(self.records)
        value = record.value
        factor = 5

        record.multiply_float(factor)
        result = record.value

        expected_value = factor * value
        self.assertEqual(result, expected_value)

    def test_zero_division(self):
        """Cannot divide by zero."""
        record = first(self.records)

        with self.assertRaises(UserError) as ue:
            record.divide_float(0)
        exc_message = ue.exception.args[0]

        self.assertIn('divide by zero', exc_message)


@tests.tagged('-standard')
class TestModelTransactionCase (tests.TransactionCase):

    def setUp(self):
        super().setUp()
        self.records = create_records(self.env, range(1, 5000))

    def test_onchange_value(self):
        """The name of the record is the string representation of its value."""
        record = first(self.records)
        value = 2.0

        record.value = value
        # Onchanges are only triggered when using Form
        self.assertNotEqual(record.name, str(value))

        record_form = Form(record)
        record_form.value = value
        record = record_form.save()

        self.assertEqual(record.name, str(value))

    def test_multiplication(self):
        """Multiplication works correctly."""
        record = first(self.records)
        value = record.value
        factor = 5

        record.multiply_float(factor)
        result = record.value

        expected_value = factor * value
        self.assertEqual(result, expected_value)

    def test_zero_division(self):
        """Cannot divide by zero."""
        record = first(self.records)

        with self.assertRaises(UserError) as ue:
            record.divide_float(0)
        exc_message = ue.exception.args[0]

        self.assertIn('divide by zero', exc_message)


@tests.tagged('post_install', '-at_install')
class TestModelTour (tests.HttpCase):
    def test_tour(self):
        tour_service = "odoo.__DEBUG__.services['web_tour.tour']"
        self.phantom_js(
            "/web",
            "%s.run('course_module_tour')" % tour_service,
            "%s.tours.course_module_tour.ready" % tour_service,
            login="admin",
        )
