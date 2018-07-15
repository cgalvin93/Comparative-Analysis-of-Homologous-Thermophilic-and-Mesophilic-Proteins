'''Takes a list of taxonomic ID's as input.
Finds all proteins in rcsb.org for each organism
Pulls desired info for each protein and organizes it into a list (pdbID, name, resolution, experimental technique, source organism)
Filters the list by keeping only the highest resolution entry for each unique protein. Also rejects proteins with resolution > 3.0 A
Filtered list is then output as a text file, along with the .pdb files for the final proteins. 
Output for each organism is placed in its own directory, the name of which is the taxonomic ID corresponding to that organism
'''
#imports
import urllib2
from pyrosetta import *
init()
from pyrosetta.toolbox import pose_from_rcsb
import os


taxidlist = [70771]	#taxID's to be searched

#function to search taxID on pdb and make a list of the pdbIDs for every entry found
def query(taxid):
	url = 'http://www.rcsb.org/pdb/rest/search'
	text1 = '''<?xml version="1.0" encoding="UTF-8"?> 
	<orgPdbQuery> 
	<version>B0907</version>
	<queryType>org.pdb.query.simple.TreeEntityQuery</queryType> 
	<description>TaxonomyTree Search for OTHER SEQUENCES</description> 
	<t>1</t> 
	<n>'''
	text2 = '''</n>
	<nodeDesc>OTHER SEQUENCES</nodeDesc> 
	</orgPdbQuery>'''
	queryText = text1 + str(taxid) + text2
	roq = urllib2.Request(url, data=queryText)
	f = urllib2.urlopen(roq)
	result = f.read()
	for i in result.split():
		pdbids.append(i)
	
#function to return the text in between two substrings within a string
def find_between( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
        

#function to pull the relevant information for each entry and organize it into a list called 'mainlist'
def fetch(pdbid):
	text1 = 'http://www.rcsb.org/pdb/rest/customReport?pdbids='
	text2 = '&customReportColumns=structureId,resolution,compound,experimentalTechnique,source&service=wsdisplay&format=xml'
	url = text1 + str(pdbid) + text2
	f = urllib2.urlopen(url)
	result = f.read()
	try:
		print result
		res = find_between(result, '<dimStructure.resolution>', '</dimStructure.resolution>')
		name = find_between(result, '<dimEntity.compound>', '</dimEntity.compound>')
		technique = find_between(result, '<dimStructure.experimentalTechnique>', '</dimStructure.experimentalTechnique>')
		source = find_between(result, '<dimEntity.source>', '</dimEntity.source>')
		mainlist.append((pdbid, name, res, technique, source))
	except:
		print "nothing for PDBID:"	+ str(pdbid)

#function to return the indices of duplicate items in an iterable:
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs	
    
#function to filter mainlist, keeping only highest res entries for each distinct protein and deleting entries with res > 3.0
def filter_strc(mainlist):
	blist = []
	for (a,b,c,e,f) in mainlist:
		blist.append(b)    					
	d = {}			
	for i in set(blist):
		value = list_duplicates_of(blist, i)	
		d[i] = value	
	clist = []
	for (a,b,c,e,f) in mainlist:
		clist.append(c) 
	delete = []
	keep = []	
	for key in d.keys():  
		cvals = []
		for x in d[key]:
			newc = clist[x]
			cvals.append(newc) 
		clow = min(cvals)
		for x in d[key]:  
			if clist[x] == clow: 
				if clow <= 3.0: 				#RESOLUTION LIMIT
					keep.append(x)
			else:  
				delete.append(x)		
	for index in sorted(delete, reverse=True):  
		del mainlist[index]		
		
#function using pyrosetta to download and clean the pdb files associated with the entries in the filtered mainlist			
def get_pdbs(mainlist):		
	finalalist = []	
	for (a,b,c,e,f) in mainlist:
		finalalist.append(str(a[0:4]))
	for pdb_id in finalalist:
		pose = pose_from_rcsb(pdb_id)			
		
#stringing everything together and organizing output into new directories for each organism:						
for i in taxidlist:
	os.mkdir(str(i))
	os.chdir(str(i))
	outfilename = str(i) + '.txt'
	ofile = open(outfilename, 'w')
	pdbids = []
	query(i)
	mainlist = []
	for i in pdbids:
		fetch(i)
	filter_strc(mainlist)
	get_pdbs(mainlist)
	for s in mainlist:
		ofile.write("%s\n" % str(s))
	ofile.close()	
	os.chdir('..')




			

		
		
					