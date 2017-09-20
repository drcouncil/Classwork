#!/user/bin/python
import csv 


def f1():

	csv_file ='Book2.csv'
	xml_fpath = 'new.xml' 
	csvData = open(csv_file,"r")
	xmlData = open(xmlFile, 'w')

	xmlData.write('<?xml version="1.0"?>' + "\n")

	xmlData.write('<csv_data>' + "\n")


def f2():

	rowNum = 0
	for row in csvData:
		if rowNum == 0:
		tags = row

for i in range(len(tags)):
 tags[i] = tags[i].replace(' ', '_')
 
 else:
 xmlData.write('</row>' + "\n")
 for i in range(len(tags)):
 xmlData.write('  ' + '<' + tags[i] + '>' \ + row[i] + '</' + tags[i] + '>' + "\n")
 
 xmlData.write('</row' + "\n")
 rowNum+=1
 
 xmlData.write('</csv_data>' + "\n")
 
 xmlData.close()

ifn__name__=="__main__":

print f1();
print f2();

