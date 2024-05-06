from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = "res.company"
	
    navbar_bg = fields.Char("Navbar Background Color")
    navbar_hover_bg = fields.Char("Navbar Hover Background Color")
    navbar_text_color = fields.Char("Navbar Text Color")
    home_bg_from = fields.Char("Home Page Gradient From")
    home_bg_to = fields.Char("Home Page Gradient To")