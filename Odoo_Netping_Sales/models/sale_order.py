# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_delivery_by = fields.Char(string="Delivery By")
    x_weight_str = fields.Char(compute='_compute_x_weight_str', string="Total Weight")
	
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
	