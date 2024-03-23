# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
	
    payment_status = fields.Selection([
        ('no', 'Not Paid'),
        ('partly', 'Partly'),
        ('done', 'Paid'),
    ], string='Payment Status', compute='_get_payment_status', readonly=True, copy=False, default='no')
    picking_status = fields.Selection([
        ('no', 'Empty'),
        ('partly', 'Partly'),
        ('done', 'Fully Done'),
    ], string='Picking Status', compute='_get_picking_status', readonly=True, copy=False, default='no')
	
    def action_poe_set_to_done(self):
        not_purchase = []
        for record in self:
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
                        res_name_match = res['name'] in ['netping.purchase.order.inherit.purchase.order.tree', 'purchase.order.form']
                        if action_match and res_name_match:
                            res['toolbar']['action'].remove(action)
        return res
		
    @api.model
    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        if 'date_planned' in vals:
            for transfer in self.env['stock.picking'].search([
                ('origin', '=', self.name),
                ('name', 'like', 'WH/IN/'),
                ('state', 'not in', ['done', 'cancel'])
            ]):
                transfer.scheduled_date = vals['date_planned']
        return res
		
    def _get_payment_status(self):
        for order in self:
            payment_states = [invoice.payment_state for invoice in order.invoice_ids if invoice.state == 'posted']
            if payment_states:
                if all([x == 'paid' for x in payment_states]):
                    order.payment_status = 'done'
                elif any([x in ['paid', 'partial'] for x in payment_states]):
                    order.payment_status = 'partly'
                else:
                    order.payment_status = 'no'
            else:
                order.payment_status = 'no'
					
    def _get_picking_status(self):
        for order in self:
            status = 'done'
            full_qty_received = 0
            products_dict = {}
            for line in order.order_line:
                if line.product_id.type != 'service':
                    if line.product_id.id not in products_dict:
                        products_dict[line.product_id.id] = [line.product_qty, line.qty_received]
                    else:
                        products_dict[line.product_id.id][0] += line.product_qty
                        products_dict[line.product_id.id][1] += line.qty_received
                    full_qty_received += line.qty_received
            if not products_dict or full_qty_received == 0:
                status = 'no'
            else:
                for id_product in products_dict:
                    if products_dict[id_product][1] < products_dict[id_product][0]:
                        status = 'partly'
                        break
            order.picking_status = status
        
