# -*- coding: utf-8 -*-
###############################################################################
#
#   email_template_header for OpenERP
#   Copyright (C) 2012 Akretion Florian da Costa <florian.dacosta@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import fields, orm

class ResCompany(orm.Model):
    _inherit = 'res.company'

    def _get_default_header_id(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        header_obj = self.pool['email.header']
        return header_obj._get_header_id(cr, uid, context=context)
            

    _columns = {
        'default_email_header_id': fields.many2one('email.header', 'Default Email Header'),
    }

    _defaults = {
        'default_email_header_id': _get_default_header_id,
    }


