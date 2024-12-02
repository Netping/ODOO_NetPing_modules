odoo.define('Odoo_Netping_Common/static/src/js/control_panel/control_panel_x2many.js', function (require) {
    'use strict';

    const { patch } = require('web.utils');
    const components = {
        ControlPanelX2Many: require('web.ControlPanelX2Many')
    };

    patch(components.ControlPanelX2Many, 'Odoo_Netping_Common/static/src/js/control_panel/control_panel_x2many.js', {
        _shouldShowPager() {
            this._super(...arguments);
            return true;
        }
    });
});