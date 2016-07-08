import xmlrpclib
import datetime

# SETUP PARAMETER
db = 'mekel-backup'
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

#BUAT KONEKSI KE NAMA OBJECT, DAN QUERY DATA
# contoh karyawan nomor id 6106

input_param = raw_input('Nomor NIK')

emp_ids = emp.execute_kw(db,uid,pwd,'hr.employee','search',[[['x_nik','=',input_param]]])
datame= emp.execute_kw(db,uid,pwd,'hr.employee','read',[emp_ids],{'fields':['name','id','street','comment','state']})
#Tampilkan data kelayar
datastate= emp.execute_kw(db,uid,pwd,'hr.employee','read',[emp_ids],{'fields':['state']})
print datastate
print datastate[0].get('state')
#Ambil waktu hari ini
print str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') )

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
if datastate[0].get('state')== 'present':
    print models.execute_kw(db, uid, pwd,'hr.attendance', 'create',[
        {'employee_id' :emp_ids[0],
         'name':datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
         'action':'sign_out'}])


if datastate[0].get('state') == 'absent':
    print models.execute_kw(db, uid, pwd,'hr.attendance', 'create',[
        {'employee_id' :emp_ids[0],
         'name':datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
         'action':'sign_in'}])
#Masukkan Kedalam absensi masuk ( Sign In)
#models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
#models.execute_kw(db, uid, pwd,'hr.attendance', 'create',[{'employee_id' :emp_ids[0],'name':datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),'action':'sign_in'}])



