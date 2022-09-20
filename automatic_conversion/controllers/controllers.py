# -*- coding: utf-8 -*-
# from odoo import http


# class AutomaticConversion(http.Controller):
#     @http.route('/automatic_conversion/automatic_conversion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automatic_conversion/automatic_conversion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('automatic_conversion.listing', {
#             'root': '/automatic_conversion/automatic_conversion',
#             'objects': http.request.env['automatic_conversion.automatic_conversion'].search([]),
#         })

#     @http.route('/automatic_conversion/automatic_conversion/objects/<model("automatic_conversion.automatic_conversion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automatic_conversion.object', {
#             'object': obj
#         })
