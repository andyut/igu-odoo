import xmlrpclib
#import datetime

# SETUP PARAMETER
db = 'mekel-backup'
url = 'http://192.168.1.131:8069'
usr = 'banay'
pwd = 'banay'
# BUAT AUTHENTIKASI
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#CEK KONEKSI DAN VERSI ODOO
print common.version()
#BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )
uid = common.authenticate(db,usr,pwd,{})
print uid
#BUAT KONEKSI KE OBJECT ODOO
emp = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

#BUAT KONEKSI KE NAMA OBJECT, DAN QUERY DATA
# contoh cari karyawan

emp_ids = emp.execute_kw(db,uid,pwd,'hr.employee','search',[[['name','ilike','ahmad'],['customer','=',1]]])

datakaryawan= emp.execute_kw(db,uid,pwd,'hr.employee','read',[emp_ids],{'fields':
                                                                            ['name',
                                                                             'id',
                                                                             'street',
                                                                             'comment',
                                                                             'x_telpon']})
print emp.execute_kw(db, uid, pwd, 'hr.employee', 'fields_get',[], {'attributes': ['string', 'help', 'type']})
#Tampilkan data kelayar
print datakaryawan
