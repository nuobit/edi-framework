# Copyright 2026 NuoBiT Solutions - Eric Antones <eantones@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from openupgradelib import openupgrade

_xmlid_renames = [
    (
        "edi_exchange_template_oca.act_open_edi_exchange_template_output_view_tree",
        "edi_exchange_template_oca.act_open_edi_exchange_template_output_view_list",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    # Odoo 18 renamed the act_window_view mode 'tree' -> 'list' and converts
    # existing ir_act_window_view rows in place, while this module renamed the
    # xmlid of its list-mode record accordingly. Without renaming the xmlid on
    # upgrade, the XML load finds no ir_model_data match and INSERTs a new row,
    # which collides with the converted one on the
    # act_window_view_unique_mode_per_action constraint.
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
