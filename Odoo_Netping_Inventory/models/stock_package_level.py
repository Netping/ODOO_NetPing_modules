# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StockPackageLevel(models.Model):
	_name = 'stock.package_level'
	_inherit = 'stock.package_level'
	
	is_done = fields.Boolean('Done', compute='_compute_is_done', inverse='_set_is_done', default=True)