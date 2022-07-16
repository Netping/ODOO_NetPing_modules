# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class MrpBom(models.Model):
    _inherit = "mrp.bom"

    x_positions = fields.Char(string="Positions")