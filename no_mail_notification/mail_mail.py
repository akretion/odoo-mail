# -*- coding: utf-8 -*-
###############################################################################
#
#   no_mail_notification for OpenERP
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

class MailMail(orm.Model):
    _inherit = 'mail.mail'

    _columns = {
        'mail_partner_ids': fields.many2many('res.partner', 'mail_partner_rel', 'mail_id', 'partner_id', string='Recipients'),
    }

    def send(self, cr, uid, ids, auto_commit=False, recipient_ids=None, context=None):
        if context is None:
            context = {}
        if recipient_ids:
            context['recipient_ids'] = recipient_ids
            context['email_ids'] = ids
        if context.get('skip_send_mail', False):
            return True
        if recipient_ids is None:
            for mail in self.browse(cr, uid, ids, context=context):
                recipient_ids = [partner.id for partner in mail.mail_partner_ids]
                break
        return super(MailMail, self).send(cr, uid, ids, auto_commit=auto_commit, recipient_ids=recipient_ids, context=context)



