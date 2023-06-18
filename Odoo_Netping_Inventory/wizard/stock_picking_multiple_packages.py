# -*- coding: utf-8 -*-

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class StockPickingMuliplePackages(models.TransientModel):
	_name = 'stock.picking.multiple.packages'
	_description = 'Stock Picking Muliple Packages'

	picking_id = fields.Many2one('stock.picking', required=True)
	location_id = fields.Many2one('stock.location', 'Source Location', check_company=True)
	location_dest_id = fields.Many2one('stock.location', 'Destination location', check_company=True)
	company_id = fields.Many2one('res.company', 'Company')
	show_operations = fields.Boolean(string="Detail Stock Operations")
	start_package_id = fields.Many2one('stock.quant.package', 'Package', required=True, check_company=True,
		domain="[('location_id', 'child_of', location_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
	stop_package_id = fields.Many2one('stock.quant.package', 'Package', required=True, check_company=True,
		domain="[('location_id', 'child_of', location_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")

	def action_done(self):
		package_list = []
		package_level_list = [x.package_id.id for x in self.picking_id.package_level_ids]
		package_level_details_list = [x.package_id.id for x in self.picking_id.package_level_ids_details]
		for package in self.env['stock.quant.package'].search([('location_id', 'child_of', self.location_id.id),
																('id', 'not in', package_level_list),
																('id', 'not in', package_level_details_list),
																('name', '>=', self.start_package_id.name),
																('name', '<=', self.stop_package_id.name),
																'|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)]):
			package_list.append((0, 0, {'picking_id': self.picking_id.id, 'package_id': package.id, 'is_done': True}))
		if not self.show_operations:
			self.picking_id.write({'package_level_ids': package_list})
		else:
			self.picking_id.write({'package_level_ids_details': package_list})
		