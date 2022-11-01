# -*- coding: utf-8 -*-
# from odoo import http


# class OdooGit(http.Controller):
#     @http.route('/odoo_git/odoo_git', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_git/odoo_git/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_git.listing', {
#             'root': '/odoo_git/odoo_git',
#             'objects': http.request.env['odoo_git.odoo_git'].search([]),
#         })

#     @http.route('/odoo_git/odoo_git/objects/<model("odoo_git.odoo_git"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_git.object', {
#             'object': obj
#         })
