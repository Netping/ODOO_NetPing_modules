# -*- coding: utf-8 -*-
{
    'name': 'Odoo_Netping_Manufacturing',
    'version': '1.1',
    'summary': 'Manufacturing Orders & BOMs',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart MRP module for Netping.

    """,
    'category': 'Manufacturing',
    'depends' : ['mrp'],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
