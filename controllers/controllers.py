# -*- coding: utf-8 -*-
# from odoo import http


# class NiletechTrading(http.Controller):
#     @http.route('/niletech_trading/niletech_trading', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/niletech_trading/niletech_trading/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('niletech_trading.listing', {
#             'root': '/niletech_trading/niletech_trading',
#             'objects': http.request.env['niletech_trading.niletech_trading'].search([]),
#         })

#     @http.route('/niletech_trading/niletech_trading/objects/<model("niletech_trading.niletech_trading"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('niletech_trading.object', {
#             'object': obj
#         })

