# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Sales',
    'version' : '1.1',
    'summary': 'Sales',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart Sales module for Netping.

    """,
    'category': 'Sales',
    'depends' : ['sale'],
    'data': [
        'views/sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
