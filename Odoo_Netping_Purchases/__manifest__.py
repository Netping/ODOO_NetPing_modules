# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Purchases',
    'version' : '1.3',
    'summary': 'Purchase',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart Purchase module for Netping.

    """,
    'category': 'Inventory/Purchase',
    'depends' : ['purchase'],
    'data': [
        'views/purchase_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
