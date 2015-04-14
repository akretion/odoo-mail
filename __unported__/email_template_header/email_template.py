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

class EmailTemplate(orm.Model):
    _inherit = 'email.template'

    def generate_email(self, cr, uid, template_id, res_id, context=None):
        if context is None:
            context = {}
        if not context.get('default_composition_mode', False):
            context['default_composition_mode'] = False
        res = super(EmailTemplate, self).generate_email(cr, uid, template_id,
                                        res_id, context=context)
        header_obj = self.pool['email.header']
        template = self.browse(cr, uid, template_id, context=context)
        header_id = header_obj._get_header_id(cr, uid,
                        model=template.model_id.model,
                        res_id=res_id, template_id=template_id,
                        context=context)
        print "zzzzzzzzzzzzzz", header_id
        if header_id:
            context['use_mail_header_id'] = header_id
        return res


