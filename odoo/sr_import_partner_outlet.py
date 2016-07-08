import requests
from  xmlrpclib import ServerProxy
import csv


url = requests.get('http://192.168.1.171/iguwebapps/app/SR_getCustomerCompany.asp')

usr = 'admin'
pwd = 'Indoguna2016'
db = 'ibom-live'


common = ServerProxy('http://192.168.1.131:8069/xmlrpc/2/common')

uid = common.authenticate(db,usr,pwd,{})
print uid

objects = ServerProxy('http://192.168.1.131:8069/xmlrpc/2/object')


test = url.iter_lines()
reader = csv.reader(test, delimiter=';')

for eachkey in reader:
    if len(eachkey)!=0:
        #print eachkey[0],eachkey[1],eachkey[17],eachkey[16],eachkey[8]
        chk_data=  objects.execute_kw(db,uid,pwd, 'res.partner','search',[[['ref','=',eachkey[0]]]])
        chk_sales=  objects.execute_kw(db,uid,pwd, 'res.users','search',[[['name','=',eachkey[6]]]])
        if len(chk_sales)==0:
            chk_sales=['1']
        if len(chk_data)==0:
            print objects.execute_kw(db,uid,pwd,
                                     'res.partner',
                                     'create',
                                     [{'vat':eachkey[1],'name':eachkey[2],
                                       'ref':eachkey[0],
                                       'company_type':'company','street':eachkey[4],
                                       'supplier':0,
                                       'customer':1,
                                       'credit_limit':eachkey[5],
                                       'user_id':chk_sales[0] }])
        else :
            print objects.execute_kw(db,uid,pwd,
                                     'res.partner',
                                     'create',
                                     [{'vat':eachkey[1],'name':eachkey[2],
                                       'company_type':'person','street':eachkey[4],
                                       'parent_id':chk_data[0],
                                       'type':'invoice',
                                       'supplier':0,
                                       'customer':1,
                                       'credit_limit':eachkey[5],
                                       'user_id':chk_sales[0] }])