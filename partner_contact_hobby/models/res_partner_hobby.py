# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartnerHobby(models.Model):

    _name = 'res.partner.hobby'
    _description = 'Res Partner Hobby'  # TODO

    name = fields.Char()

    partner_ids = fields.Many2many(
        "res.partner",
        "res_partner_hobby_rel",
        "hobby_id",
        "partner_id",
        "Partners",
        help="Partners",
    )
