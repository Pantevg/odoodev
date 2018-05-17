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


class Set_module_Tags(models.TransientModel):
    _name = 'module.tags.set'
    _description = 'Module Set Tags'

    def _default_session(self):
        return self.env['ir.module.module'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('ir.module.module',
        string="Module id:", default=_default_session, readonly=True)
    tags = fields.Many2many(
                            string='Tags',
                            comodel_name='module.tags'
                     )

    @api.multi
    def set_tags(self):
        for r in self.tags:
            self.session_id.write({'tags': [(4, [r.id])]})


#
#      _|_|_|  _|                  _|        _|            _|_|_|_|_|
#    _|            _|_|_|  _|_|    _|_|_|          _|_|          _|
#      _|_|    _|  _|    _|    _|  _|    _|  _|  _|    _|      _|
#          _|  _|  _|    _|    _|  _|    _|  _|  _|    _|    _|
#    _|_|_|    _|  _|    _|    _|  _|_|_|    _|    _|_|    _|_|_|_|_|
#