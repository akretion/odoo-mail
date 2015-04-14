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

from openerp import models, api

class EmailTemplate(models.Model):
    _inherit = 'email.template'

    @api.cr_uid_id_context
    def send_mail(self, cr, uid, template_id, res_id, force_send=False, raise_exception=False, context=None):
        header_obj = self.pool['email.header']
        ctx = context.copy()
        template = self.browse(cr, uid, template_id, context=context)
        if template.lang:
            langs = self.render_template_batch(cr, uid, template.lang, template.model, [res_id], context=context)
            if langs:
                ctx['lang'] = langs[res_id]
        header_id = header_obj._get_header_id(cr, uid,
                        model=template.model_id.model,
                        res_id=res_id, template_id=template_id,
                        context=ctx)
        if header_id:
            ctx['use_mail_header_id'] = header_id
        return super(EmailTemplate, self).send_mail(cr, uid, template_id, res_id, force_send=False, raise_exception=False, context=ctx)

