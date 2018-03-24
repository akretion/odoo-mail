# -*- coding: utf-8 -*-
# Copyright <2017> Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields
import logging
_logger = logging.getLogger(__name__)


class MailMail(models.Model):
    _inherit = 'mail.mail'

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

    @api.model
    def process_email_queue(self, ids=None):
        if self._domain_filter_defined():
            domain = self._get_domain_mail_to_really_send()
            ctx = {
                'I_really_want_to_send_this_mail': True,
                'filters': domain,
            }
            return super(MailMail, self.with_context(ctx)).process_email_queue(
                ids=ids)
        return True
