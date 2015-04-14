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

from openerp import models, fields, api, exceptions, _

class MailComposeMessage(models.TransientModel):

    _inherit = 'mail.compose.message'

    @api.multi
    def _get_header_id(self):
        header_obj = self.env['email.header']
        return header_obj._get_header_id()

    header_id = fields.Many2one(comodel_name='email.header',
                                    string = 'Default Email Header')

    @api.model
    def default_get(fields):
        result = super(MailComposeMessage, self).default_get(fields)
        header_obj = self.env['email.header']
        model = result.get('model', None)
        res_id = result.get('res_id', None)
        template_id = result.get('template_id', None)
        header_id = header_obj._get_header_id(model=model,
                        res_id=res_id, template_id=template_id)
        if model and res_id:
            record = self.pool[model].browse(cr, uid, res_id, context=context)
            result['partner_ids'] = [record.partner_id.id]
        if header_id:
            result['header_id'] = header_id
        return result

    @api.multi
    def send_mail(self):
        for wizard in self.browse(cr, uid, ids, context=context):
            if wizard.header_id:
                self._context['use_mail_header_id'] = wizard.header_id.id
        return super(MailComposeMessage, self).send_mail(cr, uid, ids,
                                                         context=context)

