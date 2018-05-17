# -*- encoding: utf-8 -*-

from openerp.osv.orm import Model
from openerp.osv import fields


class module(Model):
    _inherit = 'ir.module.module'

    # Field function Section
    def _get_all_installed_parent_ids(
            self, cr, uid, ids, field_name, arg, context=None):
        res = self._get_direct_installed_parent_ids(
            cr, uid, ids, field_name, arg, context=context)
        for id in ids:
            parent_ids = list(res[id])
            undirect_parent_ids = self._get_all_installed_parent_ids(
                cr, uid, res[id], field_name, arg, context=context)
            for parent_id in parent_ids:
                res[id] += undirect_parent_ids[parent_id]
            res[id] = list(set(res[id]))
        return res

    def _get_direct_installed_parent_ids(
            self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        imd_obj = self.pool['ir.module.module.dependency']
        for imm in self.browse(cr, uid, ids, context=context):
            imd_ids = imd_obj.search(
                cr, uid, [('name', '=', imm.name)], context=context)
            tmp = imd_obj.read(
                cr, uid, imd_ids, ['module_id'], context=context)
            imm_ids = [x['module_id'][0] for x in tmp]
            # Select only non uninstalled module
            imm_ids = self.search(
                cr, uid, [
                    ('id', 'in', imm_ids),
                    ('state', 'not in', ['uninstalled', 'uninstallable'])],
                context=context)
            res[imm.id] = imm_ids
        return res

    # Column Section
    _columns = {
        'direct_installed_parent_ids': fields.function(
            _get_direct_installed_parent_ids, type='many2many',
            relation='ir.module.module',
            string='Direct Parent Installed Modules'),
        'all_installed_parent_ids': fields.function(
            _get_all_installed_parent_ids, type='many2many',
            relation='ir.module.module',
            string='Direct and Indirect Parent Installed Modules'),
    }
