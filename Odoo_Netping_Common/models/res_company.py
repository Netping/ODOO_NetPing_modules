# -*- coding: utf-8 -*-

from odoo import api, fields, models

class WebCompanyColor(models.Model):
    _name = 'web.company.color'
	
    company_id = fields.Many2one('res.company', string="Company", required=True)
    navbar_bg = fields.Char("Navbar Background Color")
    navbar_hover_bg = fields.Char("Navbar Hover Background Color")
    navbar_text_color = fields.Char("Navbar Text Color")
    home_bg_from = fields.Char("Home Page Gradient From")
    home_bg_to = fields.Char("Home Page Gradient To")
	
    _sql_constrainst = [
        ('company_uniq', 'unique(company_id)', 'The company already has an interface setup record.'),
    ]