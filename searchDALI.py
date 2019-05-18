
###		  Automates submission of multiple chains to DALI PDB25 web server
###       Takes as input a text file with a list of pdb chains (ex. 4F80A, 58KAL), searches each chain on DALI webserver,
### 	  and returns a text file with the urls where the results for each chain can be viewed
###       USAGE: ipython searchDALI.py infile.txt outfilename.txt

import urllib
import urllib2
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

f = open(infile, 'r')
rawchains = []
for line in f.readlines()[1:]:
	chain = line[0:5] 
	rawchains.append(chain)
chainlist = []
for i in rawchains:
	if i not in chainlist and i != '\n':
		chainlist.append(i)	
f.close()

ofile = open(outfile,'w')
url = 'http://ekhidna2.biocenter.helsinki.fi/cgi-bin/sans/dump.cgi'
values = {'method' : 'pdb25',
		  'enctype' : 'multipart/form-data'}
for i in chainlist:
	values['cd1'] = str(i)
	data = urllib.urlencode(values)
	reqq = urllib2.Request(url, data)
	result = urllib2.urlopen(reqq)
	result_url = str(result.geturl()) + '\n' 
	ofile.write(result_url)
ofile.close()
print "DONE"


	
'''
SUBMIT A SINGLE REQUEST TO THE SERVER, EX CHAIN USED IS 1NT0A:
import urllib
import urllib2
url = 'http://ekhidna2.biocenter.helsinki.fi/cgi-bin/sans/dump.cgi'
values = {'cd1' : '1NTOA',
		  'method' : 'pdb25',
		  'enctype' : 'multipart/form-data'}
data = urllib.urlencode(values)
reqq = urllib2.Request(url, data)
f = urllib2.urlopen(reqq)
f.geturl()


URLLIB EXAMPLE:
import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

FROM SOURCE PAGE OF PDB25:
div id="pdb25"
form name="
name="cd1"
 name="title"
name="address"
name="method" value="pdb25">
value="Submit" name="submit" 

{'cd1' : '1NT0A',
 'method' : 'pdb25'}
 '''