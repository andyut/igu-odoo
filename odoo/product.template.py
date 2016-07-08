from  xmlrpclib import ServerProxy
import datetime

# data source  from
db = 'saranakulina-demo'
url = 'http://139.0.20.155:8069'
usr = 'admin'
pwd = 'Indoguna2016'


# data source  to

db2 = 'ibom-live'
url2 = 'http://192.168.1.131:8069'
usr2 = 'admin'
pwd2 = 'Indoguna2016'


#########################
common = ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db,usr,pwd,{})

common2 = ServerProxy('{}/xmlrpc/2/common'.format(url2))
uid2 = common2.authenticate(db2,usr2,pwd2,{})

#########################
objects = ServerProxy('{}/xmlrpc/2/object'.format(url))
objects2 = ServerProxy('{}/xmlrpc/2/object'.format(url2))
print 'User UID 2 :',uid2

#########################
oact =  objects.execute_kw(db,uid,pwd,'product.template','search',[[]])
print oact
oact_ids = objects.execute_kw(db,uid,pwd,'product.template','read',[oact],
                              {'fields':['default_code',
                                         'name',
                                         'barcode',
                                         'type',
                                         'uom_id',
                                         'uom_po_id',
                                         'tracking','list_price','standard_price'
                                         ]})
print oact_ids
img01 = objects2.execute_kw(db2,uid2,pwd2,'product.template','search',[[['default_code','=','CDN01.EMB.106']]])
img01_ids =  objects2.execute_kw(db2,uid2,pwd2,'product.template','read',[img01],{'fields':'image_medium'})

for eachkey in oact_ids :
    checkup = objects2.execute_kw(db2,uid2,pwd2,'product.template','search',[[['default_code','=',eachkey['default_code']]]])
    if len(checkup)==0 :
        print objects2.execute_kw(db2,uid2,pwd2,'product.template','create',
                            [
                                {
                                    'name':eachkey['name'],
                                    'default_code':eachkey['default_code'],
                                    'barcode':eachkey['barcode'],
                                    'type':eachkey['type'],
                                    'tracking':eachkey['tracking']
                                }
                            ])