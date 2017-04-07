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
