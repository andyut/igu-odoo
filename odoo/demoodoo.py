import xmlrpclib
import json
import csv

db = 'indoguna-procurement'
usr = 'andyut@outlook.com'
pwd = 'Indoguna2015'
url = 'https://indoguna-procurement.odoo.com'

db2 = 'procurement'
usr2 = 'admin'
pwd2 = 'admin'
url2 = 'http://192.168.1.131:8069'


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
authenticate = common2.authenticate(db2, usr2, pwd2, {})
uid2 = authenticate
print uid2


objects = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url2))
    
contacts = objects.execute_kw(db2,uid2 ,pwd2,'res.partner','search',[[['supplier','=',true]]] )
contacts_ids = objects.execute_kw(db2,uid2 ,pwd2,
                                  'res.partner','read',
                                  [contacts],{'fields':
                                              ['company_type','id',
                                               'name','parent_name',
                                               'street',
                                               'street2',
                                               'city',
                                               'phone',
                                               'mobile',
                                               'fax',
                                               'email',
                                               'supplier','customer'    ]})
print contacts_ids

objects2 = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
for eachkey in contacts_ids:
    #print eachkey
    print objects2.execute_kw(db,uid,pwd,'res.partner','create',[eachkey])


#
#leave_hr_ids = objects.execute_kw(db,uid ,pwd,'hr.holidays','read',[leave_hr],{'fields':['name','employee_id','date_from',


#customerlist =  objects.execute_kw(db,uid ,pwd,'hr.employee','read',[customerobject],{'fields':['x_nik','name']} )

