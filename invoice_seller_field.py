# -*- coding: utf-8 -*-
from openerp import api
from openerp.osv import osv, fields


class invoice_seller_field(osv.osv):
    _inherit = "account.invoice"
    _columns = {
        'seller_id': fields.selection(
            (
                ('', 'Sin Vendedor'),
                ('1', 'Vendedor 01'),
                ('2', 'Vendedor 02'),
                ('3', 'Vendedor 03'),
                ('4', 'Vendedor 04'),
                ('5', 'Vendedor 05'),
                ('6', 'Vendedor 06')
            ),
            'Seller'
        ),
    }

    _defaults = {
        'seller_id': '00'
    }

invoice_seller_field()


class pos_config(osv.osv):
    _inherit = 'pos.config'

    @api.model
    def get_sellers(self):
        result = list()
        sellers_dict = dict(self.env['account.invoice'].fields_get(allfields=['seller_id'])['seller_id']['selection'])
        for key in sorted(sellers_dict):
            temp = {}
            temp = {'seller_id': key, 'seller_name': sellers_dict[key]}
            result.append(temp)
        return result


class pos_order(osv.osv):
    _inherit = "pos.order"

    _columns = {
        'seller_id': fields.char(),
    }

    def _order_fields(self, cr, uid, ui_order, context=None):
        res = super(pos_order, self)._order_fields(cr, uid, ui_order, context)
        res.update({'seller_id': ui_order['seller_id']})
        return res

    def action_invoice(self, cr, uid, ids, context=None):
        res = super(pos_order, self).action_invoice(cr, uid, ids, context)

        inv_ref = self.pool.get('account.invoice')
        for order in self.pool.get('pos.order').browse(cr, uid, ids, context=context):
            inv_id = inv_ref.search(cr, uid, [('reference', '=', order.name)], context=context)
            inv_ref.write(cr, uid, inv_id, {'seller_id': order.seller_id}, context=context)
        return res

