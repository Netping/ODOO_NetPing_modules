# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class netping_sql_http_api(http.Controller):

    @http.route('/sqlhttpapi', methods=['POST'], auth='public', type='json')
    def run_sql(self):
        uid = False
        try:
            uid = request.session.authenticate(request.params['db'], request.params['login'], request.params['password'])
        except:
            result = {'error': 'Access Denied'}
        if uid:
            query = request.params['sql']
            if query.lower().startswith(("insert", "update", "delete")):
                result = {'error': 'No select sql'}
            else:
                request.cr.execute(query)
                result = request.cr.dictfetchall()
        return result
