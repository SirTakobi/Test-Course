odoo.define('course_module.tests', function (require) {
"use strict";

var FormView = require('web.FormView');
var testUtils = require("web.test_utils");

QUnit.module(
    'course_module',
    {
        beforeEach: function () {
            this.data = {
                record: {
                    fields: {
                        value: {
                            string: "Value",
                            type: "float",
                        },
                    },
                    records: [{
                        id: 1,
                        value: 5,
                    }]
                },
            };
        },
    },
    function () {
        QUnit.test(
            "Float value decimals",
            function (assert) {
                assert.expect(1);

                var form = testUtils.createView({
                    View: FormView,
                    model: 'record',
                    data: this.data,
                    res_id: 1,
                    arch:
                        '<form>' +
                            '<field name="value"/>' +
                        '</form>',
                });

                assert.strictEqual(
                    form.$('.o_field_widget').text(), "5.00",
                    "The value should show float with decimals");
                form.destroy();
            },
        );
    },
);
});