# -*- coding: utf-8 -*-
# © 2017 Akretion
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    availability_sent_by_mail = fields.Boolean()

    @api.model
    def _get_send_picking_availability_by_email_domain(self):
        return [
            ('state', '=', 'assigned'),
            ('availability_sent_by_mail', '=', False),
            ('picking_type_id.code', '=', 'outgoing'),
        ]

    @api.model
    def _cron_send_picking_availability(self):
        domain = self._get_send_picking_availability_by_email_domain()
        pickings = self.env['stock.picking'].search(domain)
        template = self.env.ref(
            'mail_picking_available.email_template_picking_available')
        for picking in pickings:
            template.send_mail(picking.id)
        pickings.write({'availability_sent_by_mail': True})
