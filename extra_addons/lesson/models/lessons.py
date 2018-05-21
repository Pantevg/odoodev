# -*- coding: utf-8 -*-

from openerp import models, api, fields


class LessonFirstModule(models.Model):
    _name = 'lesson.lesson'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Date')
    is_done = fields.Boolean(string='Done?')
