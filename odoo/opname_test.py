
from  xmlrpclib import ServerProxy
import datetime
import requests
import csv


usr = 'admin'
pwd = 'Indoguna2016'
db = 'ibom'


url = requests.get('http://192.168.1.171/iguwebapps/app/Produk/tranM30r-data.asp')

common = ServerProxy('http://139.0.20.155:8069/xmlrpc/2/common')
print 'common' ,common
uid = common.authenticate(db,usr,pwd,{})
print 'uid user : ',uid

objects = ServerProxy('http://139.0.20.155:8069/xmlrpc/2/object')

opname = objects.execute_kw(db,uid,pwd, 'stock.inventory','search',[[]])

opname_ids = objects.execute_kw(db,uid,pwd,'stock.inventory','read',[opname],{})


displayname= 'Opname ' +str(datetime.datetime.utcnow())
print displayname

test = url.iter_lines()
reader = csv.reader(test, delimiter=';')

opnamenew = objects.execute_kw(db,uid,pwd,
                               'stock.inventory','create',
                               [{'name':displayname,
                                 'location_id':12, 'display_name':displayname}])
for eachkey in reader:
    if len(eachkey) !=0:
        if eachkey[5]!=0:

            product = objects.execute_kw(db,uid,pwd, 'product.template','search',[[['default_code','=',eachkey[0]]]])
            product_ids = objects.execute_kw(db,uid,pwd,'product.template','read',[product],{'fields':['id','name','type','default_code','uom_id','barcode']})
            if len(product_ids) != 0:
                print objects.execute_kw(db,uid,pwd,
                                         'stock.inventory.line','create',
                                         [{'name':displayname,
                                         'inventory_id':opnamenew,'product_id':product_ids[0].get('id'),
                                         'product_name':product_ids[0].get('name')[0],
                                         'location_id':12,
                                         'product_qty':eachkey[5]}])

