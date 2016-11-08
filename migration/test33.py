from  xmlrpclib import ServerProxy
import json

def index(): return dict(message="hello from odoo_sris.py")

def faktur():return("test")

def kwitansi():return dict(message=[{'kwitansi_no':'SS20160600001',
                                    'kwitansi_date':'2016-0601',
                                    },{'kwitansi_no':'SS20160600002',
                                    'kwitansi_date':'2016-0601',
                                    },{'kwitansi_no':'SS20160600003',
                                    'kwitansi_date':'2016-0601','detail':
                                       [{'line':1,'product':'test'},
                                        {'line':2,'product':'tes2'}]
                                    }])
def invoice_list():
    db = 'sris-live'
    url = 'http://odoo.saranakulina.com:8069'
    usr = 'it-support@indoguna.co.id'
    pwd = 'Indoguna2016'
    common = ServerProxy('{}/xmlrpc/2/common'.format(url))
    objects = ServerProxy('{}/xmlrpc/2/object'.format(url))
    uid = common.authenticate(db,usr,pwd,{})
    message = 'uid = ',str(uid)
    oact =  objects.execute_kw(db,uid,pwd,'account.invoice','search',[[]])
    oact_ids = objects.execute_kw(db,uid,pwd,'account.invoice','read',[oact],{'fields':['name','code','partner_id']})
    return (oact_ids)

print type( invoice_list())