import requests
from  xmlrpclib import ServerProxy
import csv


url = requests.get('http://192.168.1.171/iguwebapps/app/obp01-data.asp')

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
        cekfirst = objects.execute_kw(db,uid,pwd,'res.partner','search',[[['ref','=',eachkey[1]]]])
        print 'check list : ',cekfirst, eachkey[1],eachkey[3]

        if len(cekfirst)==0:
            print {'comment':eachkey[2],
                                       'ref':eachkey[1],
                                       'name':eachkey[3],
                                       'street':eachkey[6],
                                       'supplier':0,
                                       'x_delivery_route':eachkey[11],
                                       'customer':1}
            print objects.execute_kw(db,uid,pwd,
                                    'res.partner','create',
                                     [{'comment':eachkey[2],
                                       'ref':eachkey[1],
                                       'name':eachkey[3],
                                       'street':eachkey[6],
                                       'supplier':0,
                                       'x_delivery_route':eachkey[11],
                                       'customer':1}])

