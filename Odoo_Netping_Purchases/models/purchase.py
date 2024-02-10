# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
	
    def action_poe_set_to_done(self):
        not_purchase = []
        for record in self:
            _logger.info(record.name)
            if record.state == 'purchase':
                record.button_done()
            else:
                not_purchase.append(record.name)
        if not_purchase:
            not_purchase_names = ", ".join(not_purchase)
            notification = {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Warning'),
                    'message': 'You cannot set to done following POE because they are not "purchase": ' + not_purchase_names,
                    'sticky': True,
                }
            }
            return notification
			
			
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(PurchaseOrder, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if toolbar:
            actions_in_toolbar = res['toolbar'].get('action')
            if actions_in_toolbar:
                for action in actions_in_toolbar:
                    if action.get('xml_id'):
                        action_match = action['xml_id'] == 'Odoo_Netping_Purchases.action_poe_set_to_done'
                        res_name_match = res['name'] == 'netping.purchase.order.inherit.purchase.order.tree'
                        if action_match and res_name_match:
                            res['toolbar']['action'].remove(action)
        return res
        
