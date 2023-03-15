# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Accounting',
    'version' : '1.2',
    'summary': 'Accounting',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for customize standart Accounting module for Netping.

    """,
    'category': 'Accounting/Accounting',
    'depends' : ['account', 'sale'],
    'data': [
        'views/account_move_views.xml',
		'views/partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
