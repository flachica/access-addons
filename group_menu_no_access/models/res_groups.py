# @author: Cesar Lage
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResGroups(models.Model):
    _inherit = "res.groups"

    menu_no_access = fields.Many2many(
        "ir.ui.menu", "ir_ui_menu_no_group_rel", "group_id", "menu_id"
    )
