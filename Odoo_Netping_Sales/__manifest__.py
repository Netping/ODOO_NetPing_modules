# -*- coding: utf-8 -*-
{
    'name' : 'Odoo_Netping_Sales',
    'version' : '2.3',
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
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
