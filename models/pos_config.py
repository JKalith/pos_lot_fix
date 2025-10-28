from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_lot_force_selection = fields.Boolean(
        string='Forzar selección de lote',
        default=True,
        help='Obliga a elegir un lote/serie en el POS cuando el producto lo requiere.'
    )
