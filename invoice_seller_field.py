# -*- coding: utf-8 -*-
from openerp import api
from openerp.osv import osv, fields

class invoice_seller_field(osv.osv):
    _inherit = "account.invoice"
    _columns = {
        'seller_id': fields.selection(
            (
                ('00', '00 - Sin Vendedor'),
                ('01', '01 - Carlos'),
                ('02', '02 - José'),
                ('03', '03 - Otro')
            ),
            'Seller'
        ),
        'cc_voucher': fields.char('Credit Card Voucher'),
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
