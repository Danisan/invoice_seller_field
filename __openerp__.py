{
    'name': "Agregado de campo custom para el vendedor en la factura",
    'version': "1.0",
    'author': "Daniel blancomartin - Blanco Martín & Asociados",
    'website': "http://www.blancomartin.com.ar",
    'category': "Tools",
    'depends': ['point_of_sale'],
    'version': '0.1',
    #'depends': ['pos'], # para el caso que se use para agregar campo en pos también
    'description': """
To practice implementation
==========================
The idea is to add a custom field to an existing module, using a written module, instead of using the developer mode and its framework.
In order to make changes easily migrable, and replicable in other instances.
""",
    'data': ['invoice_seller_field.xml'], # acá defino en el paso 5 la vista de datos
    'qweb': ['static/src/xml/pos_invoice_seller_field.xml'],
    'demo': [],
    'installable': True,
}
