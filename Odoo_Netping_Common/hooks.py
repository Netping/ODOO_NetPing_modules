# -*- coding: utf-8 -*-

from odoo import api, SUPERUSER_ID

def common_pre_init_hook(cr):
	env = api.Environment(cr, SUPERUSER_ID, {})
	# Delete East A4 portrait papeformat if exists
	paper_ids = env['report.paperformat'].search([('name', '=', 'East A4 portrait')])
	for paper in paper_ids:
		paper.sudo().unlink()
	# Delete external_layout_netping layout if exists
	extlayout_ids = env['ir.ui.view'].search([('key', '=', 'Odoo_Netping_Common.external_layout_netping')])
	for extlayout in extlayout_ids:
		extlayout.sudo().unlink()
	# Delete report.url system parameter if exists
	sys_param_ids = env['ir.config_parameter'].search([('key', '=', 'report.url')])
	for sys_param in sys_param_ids:
		sys_param.sudo().unlink()

def common_post_init_hook(cr, registry):
	env = api.Environment(cr, SUPERUSER_ID, {})
	paper = env['report.paperformat'].search([('name', '=', 'East A4 portrait')], limit=1)
	paper_id = paper.id if paper else 0
	if paper_id:
		env['res.company'].search([('id', '=', 1)]).paperformat_id = paper_id
	extlayout = env['ir.ui.view'].search([('key', '=', 'Odoo_Netping_Common.external_layout_netping')], limit=1)
	extlayout_id = extlayout.id if extlayout else 0
	if extlayout_id:
		env['res.company'].search([('id', '=', 1)]).external_report_layout_id = extlayout_id
	# Add report.url current value
	rep_url = env['ir.config_parameter'].get_param('web.base.url')
	rep_url_conf = env['ir.config_parameter'].create({'key': 'report.url', 'value': rep_url})
		