# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Mail Picking Available",
    "summary": "Sent an email when the picking is available",
    "version": "8.0.1.0.0",
    "category": "mail",
    "website": "https://odoo-community.org/",
    "author": "Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "stock",
        "mail",
    ],
    "data": [
        "data.xml",
    ],
    "demo": [
    ],
}
