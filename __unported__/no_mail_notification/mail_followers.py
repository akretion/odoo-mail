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

class MailNotification(orm.Model):
    _inherit = 'mail.notification'

    def _notify(self, cr, uid, msg_id, partners_to_notify=None, context=None):
        if context is None:
            context = {}
        context['skip_send_mail'] = True
        res = super(MailNotification, self)._notify(cr, uid, msg_id, partners_to_notify=partners_to_notify, context=context)
        print "**************", context
        if context.get('recipient_ids', False) and context.get('email_ids', False):
            self.pool['mail.mail'].write(cr, uid,
                context.get('email_ids'),
                {'mail_partner_ids': [(6, 0, context.get('recipient_ids'))]},
                context=context)
            print "kkkkkkjhhgjhghjhnkjgku", [(6, 0, context.get('recipient_ids'))]
        return res



