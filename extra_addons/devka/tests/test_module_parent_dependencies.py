# -*- encoding: utf-8 -*-

from openerp.tests.common import TransactionCase


class TestmoduleParentDependencies(TransactionCase):
    """Tests for 'Parent Dependencies module' Module"""

    def setUp(self):
        super(TestmoduleParentDependencies, self).setUp()
        self.im_obj = self.registry('ir.module.module')

    # Test Section
    def test_01_direct_parent(self):
        """Test if the compute of the field direct_parent_ids is correct."""
        cr, uid = self.cr, self.uid
        # compute expected values
        cr.execute("""SELECT module_id
            FROM ir_module_module_dependency immd
            INNER JOIN ir_module_module imm on imm.id = immd.module_id
            WHERE immd.name='base'
            AND imm.state not in ('uninstalled', 'uninstallable')""")
        expected_parent_ids = [x[0] for x in cr.fetchall()]

        # Get values
        base_id = self.im_obj.search(cr, uid, [('name', '=', 'base')])
        tmp = self.im_obj.browse(
            cr, uid, base_id)
        parent_ids = [x.id for x in tmp[0].direct_parent_ids]

        self.assertEqual(
            sorted(parent_ids), sorted(expected_parent_ids),
            "Incorrect computation of 'direct_parent_id's fields.")

    def test_02_all_parent(self):
        """Test if the compute of the field direct_parent_ids doesn't crash."""
        cr, uid = self.cr, self.uid
        base_id = self.im_obj.search(cr, uid, [('name', '=', 'base')])
        tmp = self.im_obj.browse(
            cr, uid, base_id)
        parent_ids = [x.id for x in tmp[0].all_parent_ids]

        self.assertNotEqual(
            sorted(parent_ids), [],
            "Incorrect computation of 'direct_parent_id's fields.")
