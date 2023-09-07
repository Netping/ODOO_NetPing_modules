# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Common',
    'version' : '1.3',
    'summary': 'Common',
    'author': 'Andrei Zelenin',
    'sequence': 0,
    'description': """

The specific module for general improvements for Netping.

    """,
    'category': 'Extra Tools',
    'depends' : ['mail'],
    'data': [
		'security/common_groups.xml',
        'views/common_menus.xml',
		'report/common_report_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
	'pre_init_hook': 'common_pre_init_hook',
	'post_init_hook': 'common_post_init_hook',
}
