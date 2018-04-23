from numpy import genfromtxt
import sys
import os.path
import csv
from tempfile import NamedTemporaryFile
import shutil


filename = 'file3.csv'
fieldname = 'res1'
value = 5

tempfile = NamedTemporaryFile(delete=False)

with open(filename, 'a+') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter='=')
    writer = csv.writer(tempfile, delimiter='=')
    found = False
    for row in reader:
        print(row)
        if row[0] == fieldname:
            row[1] = value
            found = True
            print('newrow' + str(row))
        writer.writerow(row)
    if not found:
        print('row not found, this added -->' + str([fieldname, value]))
        writer.writerow([fieldname, value])
shutil.move(tempfile.name, filename)
