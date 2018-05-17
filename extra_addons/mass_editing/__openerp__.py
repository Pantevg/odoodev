# -*- coding: utf-8 -*-

{
    'name': 'Mass Editing',
    'version': '8.0.2.1.0',
    'author': 'Serpent Consulting Services Pvt. Ltd., '
              'Tecnativa, '
              'Odoo Community Association (OCA)',
    'contributors': [
        'Oihane Crucelaegui <oihanecrucelaegi@gmail.com>',
        'Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>',
        'Jay Vora <jay.vora@serpentcs.com>'
    ],
    'category': 'Tools',
    'website': 'http://www.serpentcs.com',
    'license': 'GPL-3 or any later version',
    'summary': 'Mass Editing',
    'uninstall_hook': 'uninstall_hook',
    'depends': ['base'],
     'js':['src/js/*.js'],
    'data': [
        'security/ir.model.access.csv',
        'views/mass_editing_view.xml',
        'views/mass_editing_group.xml',
    ],
    'qweb': [],
    'sequence': 99,
    'installable': True,
    'application': False,
    'auto_install': False,
}
