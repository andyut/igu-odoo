import requests
from xmlrpclib import ServerProxy
import csv
from datetime import datetime

so_number=''

url_header = requests.get('http://192.168.1.171/iguwebapps/app/IGU_getSOHeader_today.asp')
url_detail = requests.get('http://192.168.1.171/iguwebapps/app/IGU_getSODetail_today.asp?docnum={}'.format(so_number))


db = 'igroup'
usr = 'admin'
pwd = 'admin'
url = 'http://192.168.1.131:8069'

common = ServerProxy('{}/xmlrpc/2/common'.format(url))
# CEK KONEKSI DAN VERSI ODOO
# print common.version()
# BUAT DATAPATKAN AUTHENTIKASI USER LOGIN ( UID )

uid = common.authenticate(db,usr,pwd,{})
# print 'User session',uid


objects = ServerProxy('{}/xmlrpc/2/object'.format(url))

objects2 = ServerProxy('{}/xmlrpc/2/object'.format(url))


test = url_header.iter_lines()
reader = csv.reader(test, delimiter=';')
for eachkey in reader:
    print eachkey
    url_detail = requests.get('http://192.168.1.171/iguwebapps/app/IGU_getSODetail_today.asp?docnum={}'.format(eachkey[11]))

    testDetail = url_detail.iter_lines()
    readerDetail = csv.reader(testDetail,delimiter=';')
    customer = objects.execute_kw(db,uid,pwd, 'res.partner','search',[[['customer','=',1],['ref','=',eachkey[2]]]])
    customer_ids = objects.execute_kw(db,uid,pwd,'res.partner','read',[customer],{'fields':['name','street']})
    if len(customer_ids) != 0:

        sales_order_header= objects.execute_kw(db,uid,pwd,'sale.order','create',[
            {'partner_id': customer_ids[0].get('id'),'validity_date':eachkey[8],
             'name':eachkey[11],'client)order_ref':eachkey[12],
             'display_name':eachkey[11]}])
        print sales_order_header
        for EachKeyDetail in readerDetail:
            print EachKeyDetail
            product = objects.execute_kw(db,uid,pwd, 'product.template','search',[[['default_code','=',EachKeyDetail[3]]]])
            product_ids = objects.execute_kw(db,uid,pwd,'product.template','read',[product],{'fields':['id','name','type','default_code','uom_id','barcode']})
            if len(product_ids) != 0 :

                print sales_order_header,EachKeyDetail[4],product_ids[0].get('uom_id')[0],EachKeyDetail[5],EachKeyDetail[8]
                objects2.execute_kw(db,uid,pwd,'sale.order.line','create',[
                    {
                        'order_id':sales_order_header,
                        'name':EachKeyDetail[4],
                        'product_id':product_ids[0].get('id'),
                        'product_uom':product_ids[0].get('uom_id')[0],
                        'product_uom_qty':EachKeyDetail[5],
                        'price_unit':EachKeyDetail[8]
                    }
                ])


