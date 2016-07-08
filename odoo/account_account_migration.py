from  xmlrpclib import ServerProxy
import datetime

# data source  from
db = 'saranakulina-demo-20160520'
url = 'http://139.0.20.155:8069'
usr = 'admin'
pwd = 'Indoguna2016'


# data source  to

db2 = 'sr-live'
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
oact =  objects.execute_kw(db,uid,pwd,'account.account','search',[[]])

oact_ids = objects.execute_kw(db,uid,pwd,'account.account','read',[oact],
                              {'fields':['name','code',
                                         'internal_type',
                                         'user_type_id',
                                         'display_name','reconcile']})
oact_idsx = objects.execute_kw(db,uid,pwd,'account.account','read',[oact],
                              {})
print oact_idsx

#########################
for eachkey in oact_ids:
     data  = objects2.execute_kw(db2,uid2,pwd2, 'account.account','search',[[['code','=',eachkey['code']]]])
     print eachkey
     if len(data)==0:
         print data
         objects2.execute_kw(db2,uid2,pwd2,
                             'account.account','create',
                             [
                                 {'code':eachkey['code'],
                                 'name':eachkey['name'] ,
                                 'internal_type':eachkey['internal_type'],
                                 'user_type_id':eachkey['user_type_id'][0],
                                 'display_name':eachkey['display_name'],
                                 'reconcile':eachkey['reconcile']}
                              ])
     else:
         print 'Already Exist '
         print data
         objects2.execute_kw(db2,uid2,pwd2,
                             'account.account','write',
                             [data,
                                 {'code':eachkey['code'],
                                 'name':eachkey['name'],
                                 'internal_type':eachkey['internal_type'],
                                 'user_type_id':eachkey['user_type_id'][0],
                                 'display_name':eachkey['display_name'],
                                 'reconcile':eachkey['reconcile']}
                              ])