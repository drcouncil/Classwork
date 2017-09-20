

#!/usr/bin/python
def f1():


	csv_fpath = 'Book2.csv'  #Ports for file
	xml_fpath = 'new.xml'
	global txts
#open the file 
	csvFile = open(csv_fpath, "r")  

	txts = [lines.strip().split(',') for lines in csvFile]

	csvFile.close()

	xmlFile = open(xml_fpath,'w')

	return txts

def f2():
#converting csv to xml
	xmlFile.write("\n" + "\t" + '<Record>') 
	xmlFile.write("\n" + "\t" + '<StudentID>' + txts[i][j]+ '</StudentID>')
	xmlFile.write("\n" + "\t" + '<FirstName>' + txts[i][j]+ '</FirstName>')
	xmlFile.write("\n" + "\t" +'<LastName>' + txts[i][j]+ '</LastName>')
	xmlFile.write("\n" + "\t" + '</Record>')
	return 

def f3():
	xmlFile.write('<?xml version="1.0"?>' + "\n")
	xmlFile.write('<Department>')
	return


def f4():
	xmlFile.write("\n"+'</Department>')

if __name__ == "__main__":
	 f1();
	 f2();
	 f3();
	 f4();

	print "Done"


if __name__=="__main__":

	print f1();
	print f2(j);


