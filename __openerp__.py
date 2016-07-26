{
    'name': "Agregado de campo custom para el vendedor en la factura",
    'author': "Daniel Blanco Martin - Blanco Martín & Asociados",
    'website': "http://www.blancomartin.com.ar",
    'category': "Tools",
    'depends': [
        'point_of_sale'
    ],
    'version': '1.2',
    'description': """
To practice implementation
==========================
The idea is to add a custom field to an existing module, using a written module, instead of using the developer mode and its framework.
In order to make changes easily migrable, and replicable in other instances.
""",
    'data': [
        'invoice_seller_field.xml',
        'security/group_seller_field_manager.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/pos_invoice_seller_field.xml'],
    'demo': [],
    'installable': True,
}
