# -*- coding: utf-8 -*-

from odoo import _, api, fields, models, SUPERUSER_ID

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _check_company_auto = True

    x_hs_code = fields.Char(string="HS-code")
	