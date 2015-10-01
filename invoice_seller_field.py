# -*- coding: utf-8 -*-
from openerp import models, fields, api
# from openerp.osv import osv, fields


class invoice_seller_field(models.Model):
    _inherit = "account.invoice"

    seller_id = fields.Selection(
        (
            ('00', '00 - Sin Vendedor'),
            ('01', '01 - Rene'),
            ('02', '02 - Guillermo'),
            ('03', '03 - Francisco'),
            ('04', '04 - Lucas'),
            ('05', '05 - Part-Time'),
            ('06', '06 - Matias')), 'Seller', default = '00')


class pos_config(models.Model):
    _inherit = 'pos.config'

    @api.model
    def get_sellers(self):
        result = list()
        sellers_dict = dict(
            self.env['account.invoice'].fields_get(
                allfields=['seller_id'])['seller_id']['selection'])
        for key in sorted(sellers_dict):
            temp = {}
            temp = {'seller_id': key, 'seller_name': sellers_dict[key]}
            result.append(temp)
        return result


class pos_order(models.Model):
    _inherit = "pos.order"

    seller_id = fields.Char()

    def _order_fields(self, cr, uid, ui_order, context=None):
        res = super(pos_order, self)._order_fields(cr, uid, ui_order, context)

        res.update({'seller_id': ui_order['seller_id']})
        return res

    def action_invoice(self, cr, uid, ids, context=None):
        res = super(pos_order, self).action_invoice(cr, uid, ids, context)

        inv_ref = self.pool.get('account.invoice')
        for order in self.pool.get('pos.order').browse(
            cr, uid, ids, context=context):
            inv_id = inv_ref.search(cr, uid, [('reference', '=', order.name)],
                context=context)
            inv_ref.write(cr, uid, inv_id, {'seller_id': order.seller_id},
                context=context)
        return res
