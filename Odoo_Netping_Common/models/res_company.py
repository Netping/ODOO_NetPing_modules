# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Company(models.Model):
    _inherit = 'res.company'

    @api.model
    def create(self, vals):
        partner = self.env['res.partner'].create({
            'name': vals['name'],
            'is_company': True,
            'image_1920': vals.get('logo'),
            'email': vals.get('email'),
            'phone': vals.get('phone'),
            'website': vals.get('website'),
            'vat': vals.get('vat'),
        })
        partner.flush()
        vals['partner_id'] = partner.id
        self.clear_caches()
        res = super(models.Model, self).create(vals)
        self.env.user.write({'company_ids': [(4, res.id)]})
        paper = self.env['report.paperformat'].search([('name', '=', 'East A4 portrait')], limit=1)
        paper_id = paper.id if paper else 0
        if paper_id:
            res.paperformat_id = paper_id
        extlayout = self.env['ir.ui.view'].search([('key', '=', 'Odoo_Netping_Common.external_layout_netping')], limit=1)
        extlayout_id = extlayout.id if extlayout else 0
        if extlayout_id:
            res.external_report_layout_id = extlayout_id
        return res


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