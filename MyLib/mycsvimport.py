from numpy import genfromtxt
import sys
import os.path
import csv
from tempfile import NamedTemporaryFile
import shutil

#filename = sys.argv[1]
#fieldname = sys.argv[2]

class MyCSVImport:

    #from mycsvimport import MyCSVImport
    #MyCSVImport.csvprop('file.csv', 'res3')

    @classmethod
    def csvgetprop(self, filename, fieldname):
        if not self.exists(filename):
            return 'File ' + filename + ' doesn t exist'
        data = genfromtxt('file.csv', delimiter='=', dtype=None)
        #return (data)
        text = ''
        for ii in range(0, len(data)):
            #print(data[ii][0])
            #text += data[ii][0] + str(data[ii][1])
            #text += fieldname.lower()
            if data[ii][0].lower() == fieldname.lower():
                #print(data[ii][1])
                return data[ii][1]
	    #return text
        return 'Property: ' + fieldname + ' in file: ' + filename +   ' NOT found.'

    # from mycsvimport import MyCSVImport
    # MyCSVImport.csvaddprop('file.csv', 'res1', 4)
    @classmethod
    def csvaddprop(self, filename, fieldname, value):
        tempfile = NamedTemporaryFile(delete=False)

        with open(filename, 'a+') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='=')
            writer = csv.writer(tempfile, delimiter='=')
            found = False
            for row in reader:
                #print(row)
                if row[0] == fieldname:
                    row[1] = value
                    found = True
                    #print('newrow' + str(row))
                writer.writerow(row)
            if not found:
                #print('row not found, this added -->' + str([fieldname, value]))
                writer.writerow([fieldname, value])
        shutil.move(tempfile.name, filename)

    @classmethod
    def exists(self, name):
        return os.path.isfile(name)
