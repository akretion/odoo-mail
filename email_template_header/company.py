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
from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_default_header_id(self):
        header_obj = self.env['email.header']
        # return an empty record because of issue https://github.com/odoo/odoo/issues/4384
        return header_obj._get_header_id() or self.env['res.company']

    default_email_header_id = fields.Many2one(comodel_name='email.header',
                                              string = 'Default Email Header',
                                              default=_get_default_header_id)
