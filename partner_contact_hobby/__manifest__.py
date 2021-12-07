# Copyright 2021 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Contact Hobby",
    "summary": """Add hobby field to contacts""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Escodoo,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/partner-contact",
    "depends": [
        "partner_contact_personal_information_page",
    ],
    "data": [
        "security/res_partner_hobby.xml",
        "views/res_partner_hobby.xml",
        "views/res_partner.xml",
    ],
    "demo": [
        "demo/res_partner_hobby.xml",
        "demo/res_partner.xml",
    ],
}
