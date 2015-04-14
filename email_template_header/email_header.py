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

class EmailHeader(models.Model):
    _name = 'email.header'

    name = fields.Char(
        string='Name',
        required=True)
    header_footer_html = fields.Html(
        string='Header/Footer',
        translate=True,
        help="Rich-text/HTML version of the header and footer."
             "You have to put a variable %s between the header "
             "and the footer. That is where the body will be inserted")

    @api.model
    def _get_header_id(self, model=None, res_id=None, template_id=None):
        "Surcharge this method to get a specific header/footer for your email"
        header_ids = self.search([])
        return header_ids and header_ids[0] or False


