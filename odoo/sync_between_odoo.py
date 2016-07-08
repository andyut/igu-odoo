import xmlrpclib
import json
import csv

# data source  from
db = 'saranakulina-demo-20160520'
url = 'http://139.0.20.155:8069'
usr = 'admin'
pwd = 'Indoguna2016'


# data source  to

db2 = 'ibom-live'
url2 = 'http://139.0.20.154:8069'
usr2 = 'admin'
pwd2 = 'Indoguna2016'



common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#CEK KONEKSI DAN VERSI ODOO
#print common.version()
#BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )
uid = common.authenticate(db,usr,pwd,{})
print 'User session',uid

common2 = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url2))
#CEK KONEKSI DAN VERSI ODOO
#print common.version()
#BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )
uid2 = common2.authenticate(db2,usr2,pwd2,{})
print uid2


objects = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

contacts = objects.execute_kw(db,uid ,pwd,'res.partner','search',[[]] )
contacts_ids = objects.execute_kw(db,uid ,pwd,
                                  'res.partner','read',
                                  [contacts],{'fields':
                                              [
                                               'name',
                                               'street',
                                               'street2',
                                               'city',
                                               'phone',
                                               'fax',
                                               'supplier','customer']})
#print contacts_ids

objects2 = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url2))
for eachkey in contacts_ids:
    #print eachkey['company_type'],eachkey['name'],eachkey['parent_name']
    data  = objects2.execute_kw(db2,uid2,pwd2, 'res.partner','search',[[['name','=',eachkey['name']]]])
    if len(data)==0 :
        print objects2.execute_kw(db2,uid2,pwd2,
                                  'res.partner','create',
                                  [{
                                      'comment':eachkey['id'],
                                      'name':eachkey['name'],
                                      'street':eachkey['street'],
                                      'street2':eachkey['street2'],
                                      'city':eachkey['city'],
                                      'phone':eachkey['phone'],
                                      'fax':eachkey['fax'],
                                      'supplier':eachkey['supplier'],
                                      'customer':eachkey['customer']
                                    }])



#
#leave_hr_ids = objects.execute_kw(db,uid ,pwd,'hr.holidays','read',[leave_hr],{'fields':['name','employee_id','date_from',


#customerlist =  objects.execute_kw(db,uid ,pwd,'hr.employee','read',[customerobject],{'fields':['x_nik','name']} )

