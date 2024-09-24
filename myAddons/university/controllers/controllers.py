from operator import index

from odoo import http
from odoo.http import request


class University(http.Controller):
    @http.route('/university', type='http', auth='public', website=True)
    def index(self, **kw):
        university_data = request.env['university.student'].sudo().search([])
        values = {
            'record': university_data
        }
        return request.render('university.site_web_university', values)

    # @http.route('/university/university/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('university.listing', {
    #         'root': '/university/university',
    #         'objects': http.request.env['university.university'].search([]),
    #     })
    #
    # @http.route('/university/university/objects/<model("university.university"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('university.object', {
    #         'object': obj
    #     })

