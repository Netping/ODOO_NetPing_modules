# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Inventory',
    'version' : '1.3',
    'summary': 'Manage your stock and logistics activities',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart Inventory module for Netping.

    """,
    'category': 'Inventory',
    'depends' : ['stock'],
    'data': [
	    'views/product_views.xml',
		'views/stock_quant_views.xml',
        'views/stock_picking_views.xml',
		'views/stock_menu_views.xml',
		'views/stock_orderpoint_views.xml',
		'views/stock_scrap_views.xml',
		'views/stock_move_line_views.xml',
		'wizard/stock_scheduler_compute_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
