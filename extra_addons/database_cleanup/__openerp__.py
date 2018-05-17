# -*- coding: utf-8 -*-

{
    'name': 'Database cleanup',
    'version': '8.0.0.1.0',
    'author': "Therp BV,Odoo Community Association (OCA)",
    'depends': ['base'],
    'license': 'AGPL-3',
    'category': 'Tools',
    'data': [
        'view/purge_menus.xml',
        'view/purge_modules.xml',
        'view/purge_models.xml',
        'view/purge_columns.xml',
        'view/purge_tables.xml',
        'view/purge_data.xml',
        'view/menu.xml',
        ],
    'sequence': 99,
}
