# -*- coding: utf-8 -*-

#######################################################
#                                                     #
#                  Let my BUGS GO !!!                  #
#                                                       #
#                               m                        #
#           $m                mm            m             #
#            "$mmmmm        m$"    mmmmmmm$"               #
#                  """$m   m$    m$""""""                   #
#                mmmmmmm$$$$$$$$$"mmmm                       #
#          mmm$$$$$$$$$$$$$$$$$$ m$$$$m  "    m  "            #
#        $$$$$$$$$$$$$$$$$$$$$$  $$$$$$"$$$                    #
#         mmmmmmmmmmmmmmmmmmmmm  $$$$$$$$$$
#         $$$$$$$$$$$$$$$$$$$$$  $$$$$$$"""  m
#         "$$$$$$$$$$$$$$$$$$$$$ $$$$$$  "      "
#             """""""$$$$$$$$$$$m """"
#               mmmmmmmm"  m$   "$mmmmm                                  _##
#             $$""""""      "$     """"""$$                           _##
#           m$"               "m           "                       _##
#                               "                               _##
#                                                            _##
#             ****** KoroVieV-f@gOt ******                _##
#                                                      _##
#######################################################


from openerp import models, api, fields
import datetime

import logging  #Get the logger

_logger = logging.getLogger(__name__) #Get the logger

class module(models.Model):
    _inherit = 'ir.module.module'

    inst_id = fields.Many2one('ir.module.module')
    upg_id = fields.Many2one('ir.module.module')
    uninst_id = fields.Many2one('ir.module.module')
    inst2_id = fields.Many2one('ir.module.module')
    upg2_id = fields.Many2one('ir.module.module')
    uninst2_id = fields.Many2one('ir.module.module')
    tags = fields.Many2many(
                            string='Tags',
                            comodel_name='module.tags')

    @api.one
    def clear_tags(self):
        self.tags = False


class moduleRelease(models.Model):
    _name = "module.release"

    @api.one
    @api.onchange('devka_ins_id', 'devka_upg_id', 'devka_uninst_id', 'devka2_ins_id', 'devka2_upg_id', 'devka2_uninst_id')
    def _compute_count(self):
        ins = self.devka_ins_id
        upg = self.devka_upg_id
        unins = self.devka_uninst_id
        ins2 = self.devka2_ins_id
        upg2 = self.devka2_upg_id
        unins2 = self.devka2_uninst_id
        self.ins_count_1 = len(ins)
        self.upg_count_1 = len(upg)
        self.unins_count_1 = len(unins)
        self.ins_count_2 = len(ins2)
        self.upg_count_2 = len(upg2)
        self.unins_count_2 = len(unins2)

    ins_count_1 = fields.Integer('To install #1:', compute=_compute_count)
    upg_count_1 = fields.Integer('To upgrade #1:', compute=_compute_count)
    unins_count_1 = fields.Integer('To Unstall #1:', compute=_compute_count)
    ins_count_2 = fields.Integer('To install #2:', compute=_compute_count)
    upg_count_2 = fields.Integer('To upgrade #2:', compute=_compute_count)
    unins_count_2 = fields.Integer('To Unstall #2:', compute=_compute_count)

    name = fields.Char("Release #:")
    info = fields.Text('Description:')
    info2 = fields.Text('Description #1:')
    info3 = fields.Text('Description #2:')
    is_update = fields.Boolean('is Actual?', default=True)
    bug_free = fields.Boolean('Stage #2? :', default=False)
    dt_date = fields.Datetime('Release Date', default=datetime.datetime.now())

    devka_ins_id = fields.One2many('ir.module.module', 'inst_id')
    devka_upg_id = fields.One2many('ir.module.module', 'upg_id')
    devka_uninst_id = fields.One2many('ir.module.module', 'uninst_id')
    devka2_ins_id = fields.One2many('ir.module.module', 'inst2_id')
    devka2_upg_id = fields.One2many('ir.module.module', 'upg2_id')
    devka2_uninst_id = fields.One2many('ir.module.module', 'uninst2_id')

    @api.multi
    def inst_all_1(self):
        x = self.devka_ins_id
        for r in x:
            if r.state == 'uninstalled':
                _logger.info('---------INSTALLING------> %s', r.name)
                r.button_immediate_install()
                _logger.info('---------installed->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------Already Installed------> %s', r.name)
                pass

    @api.multi
    def upg_all_1(self):
        x = self.devka_upg_id
        for r in x:
            if r.state == 'installed':
                _logger.info('---------UPGRADING------> %s', r.name)
                r.button_immediate_upgrade()
                _logger.info('---------upgraded->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------INSTALLING------> %s', r.name)
                r.button_immediate_install()
                _logger.info('---------installed->>>>>>>>>> %s', r.name)

    @api.multi
    def uninst_all_1(self):
        x = self.devka_uninst_id
        for r in x:
            if r.state == 'installed':
                _logger.info('---------UnInstalling------> %s', r.name)
                r.button_immediate_uninstall()
                _logger.info('---------UnInstalled->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------Already UnInstalled------> %s', r.name)
                pass

    @api.multi
    def inst_all_2(self):
        x = self.devka2_ins_id
        for r in x:
            if r.state == 'uninstalled':
                _logger.info('---------INSTALLING------> %s', r.name)
                r.button_immediate_install()
                _logger.info('---------installed->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------Already Installed------> %s', r.name)
                pass

    @api.multi
    def upg_all_2(self):
        x = self.devka2_upg_id
        for r in x:
            if r.state == 'installed':
                _logger.info('---------UPGRADING------> %s', r.name)
                r.button_immediate_upgrade()
                _logger.info('---------upgraded->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------INSTALLING------> %s', r.name)
                r.button_immediate_install()
                _logger.info('---------installed->>>>>>>>>> %s', r.name)

    @api.multi
    def uninst_all_2(self):
        x = self.devka2_uninst_id
        for r in x:
            if r.state == 'installed':
                _logger.info('---------UnInstalling------> %s', r.name)
                r.button_immediate_uninstall()
                _logger.info('---------UnInstalled->>>>>>>>>> %s', r.name)
            else:
                _logger.info('---------Already UnInstalled------> %s', r.name)
                pass


class module_dependency(models.Model):
    _inherit = 'ir.module.module.dependency'

    author = fields.Char('Author', compute='_compute_author')

    @api.one
    @api.depends('depend_id.author')
    def _compute_author(self):
        self.author = self.depend_id.author or 'unknown'

    @api.multi
    def dt_button_install(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_install()
        return True

    @api.multi
    def dt_button_immediate_upgrade(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_upgrade()
        return True

    @api.multi
    def dt_button_uninstall(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_uninstall()
        return True


class ModuleTags(models.Model):
    _name = 'module.tags'

    name = fields.Char(string='Name')


#
#      _|_|_|  _|                  _|        _|            _|_|_|_|_|
#    _|            _|_|_|  _|_|    _|_|_|          _|_|          _|
#      _|_|    _|  _|    _|    _|  _|    _|  _|  _|    _|      _|
#          _|  _|  _|    _|    _|  _|    _|  _|  _|    _|    _|
#    _|_|_|    _|  _|    _|    _|  _|_|_|    _|    _|_|    _|_|_|_|_|
#


