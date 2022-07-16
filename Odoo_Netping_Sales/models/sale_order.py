# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_delivery_by = fields.Char(string="Delivery By")