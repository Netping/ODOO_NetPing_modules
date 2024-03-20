# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_delivery_by = fields.Char(string="Delivery By")
    x_weight_str = fields.Char(compute='_compute_x_weight_str', string="Total Weight")
	
    payment_status = fields.Selection([
        ('no', 'Not Paid'),
        ('partly', 'Partly'),
        ('done', 'Paid'),
    ], string='Payment Status', compute='_get_payment_status', store=True, readonly=True, copy=False, default='no')
    picking_status = fields.Selection([
        ('no', 'Empty'),
        ('partly', 'Partly'),
        ('done', 'Fully Done'),
    ], string='Picking Status', compute='_get_picking_status', store=True, readonly=True, copy=False, default='no')
	
    def _prepare_confirmation_values(self):
        return {
            'state': 'sale'
        }
		
    @api.depends('order_line')
    def _compute_x_weight_str(self):
        for order in self:
            order_weight = 0.00
            for line in order.order_line:
                if line.x_weight == 0:
                    order_weight = 0.00
                    break					
                order_weight += line.x_weight * line.product_uom_qty
            order.x_weight_str = str(round(order_weight, 2)) if order_weight else '-'
			
    @api.depends('invoice_ids')
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
					
    @api.depends('order_line')
    def _get_picking_status(self):
        res = 'done'
        for order in self:
            status_list = ['no', 'partly', 'done']
            full_qty_delivered = 0
            for line in order.order_line:
                full_qty_delivered += line.qty_delivered
                if line.product_uom_qty > 0 and line.qty_delivered < line.product_uom_qty:
                    if 'done' in status_list:
                        status_list.pop()
            if full_qty_delivered == 0:
                status_list.pop()
            order.picking_status = status_list.pop()

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    x_hs_code = fields.Char(string="HS-code", related="product_id.product_tmpl_id.x_hs_code")
    x_weight = fields.Float(string="Weight", related="product_id.weight")
    x_line_weight_str = fields.Char(compute='_compute_x_line_weight_str', string="Weight")

    @api.depends('x_weight')
    def _compute_x_line_weight_str(self):
        for line in self:
            line_weight = round(line.x_weight * line.product_uom_qty, 2)
            line.x_line_weight_str = str(line_weight) if line_weight else '-'
	