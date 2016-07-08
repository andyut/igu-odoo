import requests
import csv



def getcustomer():
    # AMBIL DATA CUSTOMER
    url = requests.get('http://192.168.1.171/iguwebapps/app/SR_getCustomerOutlet.asp')
    test = url.iter_lines()
    reader = csv.reader(test, delimiter=';')
    return reader


def getProduct():
    # AMBIL DATA PRODUCT
    url = requests.get('http://192.168.1.171/iguwebapps/app/Produk/tranM30r-data.asp')
    test = url.iter_lines()
    reader = csv.reader(test, delimiter=';')
    return reader
