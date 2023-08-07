# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class AccountMove(models.Model):
    _inherit = "account.move"

    x_doc_type = fields.Selection([('manufacture', 'Manufacture'), ('service', 'Service'), ('lintech', 'Lintech')], string="Type", required=True)
    x_GUI = fields.Char(string="Taiwan GUI number")
    x_GUI_date = fields.Date(string="GUI date")