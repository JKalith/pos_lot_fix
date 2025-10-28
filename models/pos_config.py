# -*- coding: utf-8 -*-
from odoo import models, fields

class PosConfig(models.Model):
    _inherit = "pos.config"

    pos_lot_force_selection = fields.Boolean(
        string="Forzar selección de lote",
        default=True,
        help="Si está activado, el POS obligará a elegir un lote/serie en productos que lo requieran."
    )
