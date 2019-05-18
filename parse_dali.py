#######     OPENS RESULTS OF DALI SEARCH FOR A GIVEN PROTEIN CHAIN AND 
#######     PARSES FOR HOMOLOGOUS CHAINS
#######		USAGE: ipython parse_dali2.py chainlist.txt urllist.txt outfilename.txt

import urllib
import urllib2
import sys

chainfile = sys.argv[1]
urlfile = sys.argv[2]
outfilename = sys.argv[3]

#create list of chain IDs from text file:
cf = open(chainfile, 'r')
rawchains = []
for line in cf.readlines()[1:]:
	chain = line[0:5] 
	rawchains.append(chain)
chainlist = []
for i in rawchains:
	if i not in chainlist and i != '\n':
		chainlist.append(i)	
cf.close()

#create list of result urls from text file:
uf = open(urlfile, 'r')
urllist = []
for line in uf.readlines():
	link = str(line)
	urllist.append(link)
uf.close()

#the parseable version of the results is the result url with 'chainID.txt' at the end rather than 'index.html'
#make list of parseable result urls:
result_url_list = []
for i in urllist:
	first_part = i[0:65]
	chain_index = urllist.index(i)
	cc = chainlist[chain_index]
	cc1 = cc[0:4]
	cc2 = cc[4]
	second_part = cc1.lower() + cc2
	result_url = first_part + second_part + '.txt'
	result_url_list.append(result_url)


#parse the results for each chain and write homologues to a text file:
ofile = open(outfilename, 'w')
for x in result_url_list:
	url = str(x)
	try:
		result = urllib2.urlopen(url)
		query_ptn = '\n' + result.readlines()[1] 
		ofile.write(query_ptn)
		result = urllib2.urlopen(url)
		table_header = result.readlines()[2]
		ofile.write(table_header)
		result = urllib2.urlopen(url)
		for line in result.readlines()[3:]:
			Z_scr = line[14:18]
			RMSD = line[20:23]
			ID = line[35:39]
			try:
				if float(Z_scr) >= 8.0 and float(RMSD) <= 4.0 and 30 <=int(ID) < 75:
					ofile.write(line + '\n')
				else:
					continue
			except:
				pass	
	except: 
		print "Could not open " + url			
ofile.close()			
	
	



	
