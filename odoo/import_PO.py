import xmlrpclib
import json
import csv

db = 'ibom'
usr = 'andyut@indoguna.co.id'
pwd = 'Indoguna2016'
url = 'http://139.0.20.155:8069'

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
uid2 = common2.authenticate(db2,usr2,pwd2,{})
print uid2

objects = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
objects2 = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url2))

data= objects2.execute_kw(db2,uid2,pwd2,'purchase.order','search',[[]])
data_ids = objects2.execute_kw(db2,uid2,pwd2,
                               'purchase.order','read',
                               [data],
                               {'fields':
                                ['name','id',
                                 'partner_id',
                                 'date_order','comment'
                                 ]})


#print data_ids

#look= objects.execute_kw(db,uid,pwd,'account.invoice','search',[[]])
#print objects.execute_kw(db,uid,pwd,'account.invoice','read',[look],{})
for eachkey in data_ids:
    #print eachkey['name'], eachkey['partner_id'][1], eachkey['date_order']
    lookup = objects.execute_kw(db,uid,pwd,'res.partner','search',[[['comment','=',eachkey['partner_id'][0]]]])
    #print lookup
    if lookup:
        ap_invoice = objects.execute_kw(db,uid,pwd,'account.invoice','create',[
            {'name':eachkey['name'],'type':'in_invoice',
             'partner_id':lookup[0],
             'date_invoice':eachkey['date_order']}])

        purchase_detail= objects2.execute_kw(db2,uid2,pwd2,'purchase.order.line','search',[[['order_id','=',eachkey['id']]]])
        purchase_detail_ids = objects2.execute_kw(db2,uid2,pwd2,
                                                  'purchase.order.line','read',
                                                  [purchase_detail],{'fields':['invoice_id','display_name',
                                                                    'name',
                                                                    'product_qty','price_unit','price_total']})


        for eachdetail in purchase_detail_ids:
            print  objects.execute_kw(db,uid,pwd,'account.invoice.line','create',[
                {'name':eachdetail['name'],
                 'invoice_id': ap_invoice,'account_id':25,
                 'quantity':eachdetail['product_qty'],
                 'price_unit':eachdetail['price_unit'],
                 'price_subtotal':eachdetail['price_total']
                 }])