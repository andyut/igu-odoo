import xmlrpclib


# SETUP PARAMETER
db = 'saranakulina-demo'
url = 'http://192.168.1.131:8069'
usr = 'admin'
pwd = 'admin'
# BUAT AUTHENTIKASI
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#CEK KONEKSI DAN VERSI ODOO
print common.version()
#BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )
uid = common.authenticate(db,usr,pwd,{})
print uid
#BUAT KONEKSI KE OBJECT ODOO
emp = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

stockpick = emp.execute_kw(db,uid,pwd,'stock.picking','search',[[]])
stockpick_ids = emp.execute_kw(db,uid,pwd,
                               'stock.picking','read',
                               [stockpick],{'fields':
                                            ['location_id',
                                             'location_dest_id',
                                             'partner_id',
                                             'min_date',
                                             'pack_operation_product_ids']})
print stockpick_ids

stockpick2 = emp.execute_kw(db,uid,pwd,'stock.pack.operation','search',[[]])
stockpick2_ids = emp.execute_kw(db,uid,pwd,
                               'stock.pack.operation','read',
                               [stockpick],{})

print 'testing \n',stockpick2_ids