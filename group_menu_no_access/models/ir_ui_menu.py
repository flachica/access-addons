# @author: Fernando La Chica
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import SUPERUSER_ID, api, fields, models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    no_groups = fields.Many2many(
        "res.groups", "ir_ui_menu_no_group_rel", "menu_id", "group_id"
    )

    @api.returns("self")
    def _filter_visible_menus(self):
        menus = super(IrUiMenu, self)._filter_visible_menus()

        if self.env.user.id != SUPERUSER_ID:
            groups = self.env.user.groups_id
            menus = menus.filtered(lambda menu: not (menu.no_groups & groups))
        return menus
