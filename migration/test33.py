from  xmlrpclib import ServerProxy
import datetime

# data source  from
db = 'sris-live'
url = 'http://139.0.20.155:8069'
usr = 'it-support@indoguna.co.id'
pwd = 'Indoguna2016'


#########################
common = ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db,usr,pwd,{})

print "uid ",uid