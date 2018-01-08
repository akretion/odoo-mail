# -*- coding: utf-8 -*-
# Copyright <2017> Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Mail Picking Available",
    "summary": "Sent an email when the picking is available",
    "version": "10.0.1.0.0",
    "category": "mail",
    "website": "https://odoo-community.org/",
    "author": "Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "mail",
    ],
    "data": [
        "data/data.xml",
    ],
}
