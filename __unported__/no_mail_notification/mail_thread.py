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

class MailThread(orm.AbstractModel):
    _inherit = 'mail.thread'

    def message_track(self, cr, uid, ids, tracked_fields, initial_values, context=None):
        if context is None:
            context = {}
        context['skip_message_creation'] = True
        res = super(MailThread, self).message_track(cr, uid, ids, tracked_fields, initial_values, context=context)

    def message_post(self, cr, uid, thread_id, body='', subject=None, type='notification',
                        subtype=None, parent_id=False, attachments=None, context=None,
                        content_subtype='html', **kwargs):
        if context is None:
            context = {}
        if context.get('skip_message_creation', False):
            return False
        return super(MailThread, self).message_post(cr, uid, thread_id, body=body,
                                                   subject=subject, type=type, subtype=subtype,
                                                   parent_id=parent_id, attachments=attachments,
                                                   context=context, content_subtype=content_subtype, **kwargs)


