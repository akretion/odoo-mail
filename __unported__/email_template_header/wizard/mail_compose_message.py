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

class MailComposeMessage(orm.TransientModel):

    _inherit = 'mail.compose.message'

    def _get_header_id(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        header_obj = self.pool['email.header']
        return header_obj._get_header_id(cr, uid, context=context)

    _columns = {
        'header_id': fields.many2one('email.header', 'Default Email Header'),
    }

    def default_get(self, cr, uid, fields, context=None):
        if context is None:
            context = {}
        result = super(MailComposeMessage, self).default_get(cr, uid, fields, context=context)
        header_obj = self.pool['email.header']
        model = result.get('model', None)
        res_id = result.get('res_id', None)
        template_id = result.get('template_id', None)
        header_id = header_obj._get_header_id(cr, uid, model=model,
                        res_id=res_id, template_id=template_id,
                        context=context)
        if model and res_id:
            record = self.pool[model].browse(cr, uid, res_id, context=context)
            result['partner_ids'] = [record.partner_id.id]
        if header_id:
            result['header_id'] = header_id
        return result

    def send_mail(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        for wizard in self.browse(cr, uid, ids, context=context):
            if wizard.header_id:
                context['use_mail_header_id'] = wizard.header_id.id
        return super(MailComposeMessage, self).send_mail(cr, uid, ids,
                                                         context=context)

