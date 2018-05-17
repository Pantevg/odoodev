# -*- coding: utf-8 -*-

{
    'name': 'DEV_KA',
    'author':   'Alexa',
    'maintainer': 'Alexa',
    'summary': 'Custom Developer tweeks (FOR QArea Theme)',
    'category': 'Tools',
    'website': 'http://www.hzsho.in.ua',
    'version': '08.0.2.1.0',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base', 'web'],
    'data': [
        'wizard/module_set_tags.xml',
        'views/dev_view.xml',
        'views/action_dev.xml',
        'views/release.xml',
        'security/ir.model.access.csv',
            ],

    'installable': True,
    'auto_install': False
}
