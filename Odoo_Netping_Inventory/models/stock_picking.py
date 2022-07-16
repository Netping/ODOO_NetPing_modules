# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class Picking(models.Model):
    _inherit = "stock.picking"

    x_GUI = fields.Char(string="Taiwan GUI number")
    x_GUI_date = fields.Date(string="GUI date")