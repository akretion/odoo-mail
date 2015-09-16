# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2015 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
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

from openerp import models, api, fields
import logging
_logger = logging.getLogger(__name__)


class MailMail(models.Model):
    _inherit='mail.mail'

    spamoo_blocked = fields.Boolean()

    @api.multi
    def send(self, auto_commit=False, raise_exception=False):
        if self._context.get('I_really_want_to_send_this_mail'):
            return super(MailMail, self).send(
                auto_commit=auto_commit,
                raise_exception=raise_exception)
        else:
            _logger.error("Spamoo have tried to send an email!")
            self.write({'spamoo_blocked': True})
        return True

    @api.multi
    def send_for_real(self):
        return self.with_context(I_really_want_to_send_this_mail=True).send()

    @api.model
    def _get_domain_mail_to_really_send(self):
        return []

    @api.model
    def _domain_filter_defined(self):
        return False

    @api.cr_uid
    def process_email_queue(self, cr, uid, ids=None, context=None):
        if self._domain_filter_defined(cr, uid, context=context):
            domain = self._get_domain_mail_to_really_send(
                cr, uid, context=context)
            if context is None:
                context={}
            context.update({
                'I_really_want_to_send_this_mail': True,
                'filters': domain,
                })
            return super(MailMail, self).process_email_queue(
                cr, uid, ids=ids, context=context)
        return True
