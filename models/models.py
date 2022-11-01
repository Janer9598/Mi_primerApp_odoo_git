# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo_git(models.Model):
#     _name = 'odoo_git.odoo_git'
#     _description = 'odoo_git.odoo_git'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
