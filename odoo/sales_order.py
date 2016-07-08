import xmlrpclib
import datetime

db = 'saranakulina-demo'
usr = 'admin'
pwd = 'admin'
url = 'http://192.168.1.131:8069'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#CEK KONEKSI DAN VERSI ODOO
#print common.version()
#BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )
uid = common.authenticate(db,usr,pwd,{})
print 'User session',uid

objects  = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

salesorder = objects.execute_kw(db,uid,pwd, 'sale.order','search',[[]])
print 'sales order serach ',salesorder
print 'detail \n'
print objects.execute_kw(db,uid,pwd,'sale.order','read',[salesorder],{'fields':
                                                                      ['name',
                                                                       'id',
                                                                       'order_line']})