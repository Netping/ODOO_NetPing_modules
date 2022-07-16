# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Inventory',
    'version' : '1.1',
    'summary': 'Manage your stock and logistics activities',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart Inventory module for Netping.

    """,
    'category': 'Inventory',
    'depends' : ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
