import csv
import requests

url = 'http://192.168.1.171/iguwebapps/app/Tally-data.asp?'
r = requests.get(url)
text = r.iter_lines()
reader = csv.reader(text, delimiter=';')
print reader
for row in reader:
    print row[6],row[9],row[2],row[3],row[8],row[10],row[5]