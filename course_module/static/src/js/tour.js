odoo.define('course_module.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register(
    'course_module_tour',
    {
        url: "/web",
    },
    [
        tour.STEPS.SHOW_APPS_MENU_ITEM,
        {
            trigger: '.o_app[data-menu-xmlid="course_module.course_module_model_menu"]',
            content: _t("Open the course app."),
            position: 'right',
        },
        {
            trigger: '.o_list_button_add',
            content: _t("Create a new record."),
            position: 'right',
        },
        {
            trigger: 'input[name="value"]',
            content: _t("Insert a value."),
            position: 'right',
            run: 'text 5',
        },
        {
            trigger: '.o_form_button_save',
            content: _t("Save."),
            position: 'right',
        },
        {
            trigger: ".breadcrumb-item:not(.active):last",
            content: _t("Go back."),
            position: "right",
        },
    ],
);

});
