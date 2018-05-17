# -*- coding: utf-8 -*-

from openerp import models, api, fields


class StudyFirstModule(models.Model):
    _name = 'study.study'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    is_done = fields.Boolean(string='Done')
