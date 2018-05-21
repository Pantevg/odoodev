# -*- coding: utf-8 -*-

from openerp import models, api, fields


class BazaFirstModule(models.Model):
    _name = 'baza.baza'

    category = fields.Char(string='Category')
    question = fields.Char(string='Question')
    date_article = fields.Date(string='Date')
    answer = fields.Text(string='Answer')
    actual = fields.Boolean(string='Actual?')
