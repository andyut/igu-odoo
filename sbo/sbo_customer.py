import requests
import csv



def getCustomer():
    url = requests.get('http://192.168.1.171/iguwebapps/app/obp01-data.asp')



    test = url.iter_lines()
    reader = csv.reader(test, delimiter=';')

    return reader

for eachkey in  getCustomer():
    print eachkey



