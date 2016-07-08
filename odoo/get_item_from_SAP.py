import requests
from  xmlrpclib import ServerProxy
import csv


url = requests.get('http://192.168.1.171/iguwebapps/app/Produk/tranM30r-data.asp')

usr = 'admin'
pwd = 'admin'
db = 'igroup'


common = ServerProxy('http://192.168.1.131:8069/xmlrpc/2/common')

uid = common.authenticate(db,usr,pwd,{})
print uid

objects = ServerProxy('http://192.168.1.131:8069/xmlrpc/2/object')


test = url.iter_lines()
reader = csv.reader(test, delimiter=';')

for eachkey in reader:
    if len(eachkey)!=0:
        #print eachkey[0],eachkey[1],eachkey[17],eachkey[16],eachkey[8]
        chk_data=  objects.execute_kw(db,uid,pwd, 'product.template','search',[[['default_code','=',eachkey[0]]]])
        if len(chk_data)==0:
            print objects.execute_kw(db,uid,pwd,
                                     'product.template',
                                     'create',
                                     [{'name':eachkey[1],'default_code':eachkey[0],
                                       'standard_price':eachkey[8],
                                       'qty_available':eachkey[6]}])
        else :
           print objects.execute_kw(db,uid,pwd,
                                     'product.template',
                                     'write',
                                     [chk_data,{'name':eachkey[1],'default_code':eachkey[0],
                                       'standard_price':eachkey[8]}])
