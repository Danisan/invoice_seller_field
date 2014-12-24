from openerp.osv import osv,fields
class invoice_seller_field(osv.osv):
    _inherit = "account.invoice"
    _columns = {
        'seller_id': fields.selection(
        	(
        		('00','00 - Sin Vendedor'),
        		('01','01 - Carlos'),
        		('02','02 - José'),
        		('03','03 - Otro')
        	),
           'Seller'
        ),
    }
    _defaults ={
        'seller_id': '00'
    }
invoice_seller_field()
