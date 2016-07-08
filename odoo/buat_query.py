import xmlrpclib
import datetime

# SETUP PARAMETER
db = 'saranakulina-demo-20160520'
url = 'http://139.0.20.155:8069'
usr = 'admin'
pwd = 'Indoguna2016'
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

data_ids = emp.execute_kw(db,uid,pwd,'res.users','search',[[]])

data= emp.execute_kw(db,uid,pwd,'res.users','read',[data_ids],{'fields':['name','login']})
#print emp.execute_kw(db, uid, pwd, 'stock.pack.operation', 'fields_get',[], {})
#Tampilkan data kelayar
print data[0].values()[0]
for eachkey in data :
    print eachkey.values()
