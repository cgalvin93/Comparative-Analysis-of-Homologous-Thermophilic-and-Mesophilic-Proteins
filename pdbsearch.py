'''
Searches rcsb.org by source organism using taxonomic IDs
returns pdbIDs and unique chains of all high quality, 
nonredundant structures available for each organism.


'''
#list of taxIDs to be searched	
taxidlist = [43687,354255,2261,184117,1927912,54252,56636,111955,2320,169300,63363,2269,76887,62609,70771,2271,2234,84156,2180,
			 2181,444093,52765,55205,67760,29344,2190,14,246264,92642,213185,29549,119072,200415,111519,93930,105851,
			 171869,336261,271,3282676,41675,31899,2285,43080,2287,2336,311400,2336]
			 
import os 			
import Bio
from Bio.PDB import PDBList
from Bio.PDB.MMCIF2Dict import MMCIF2Dict 
import urllib2

#function to search taxonomic ID on rcsb and 
#make a list of the pdbIDs for every entry found
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
		pdbids.append(str(i)[0:4])

#function to filter out bad quality structures 	
def filter_bad_strc(pdbID):
	d = MMCIF2Dict(pdbID + '.cif')	
	try:
		method = d['_exptl.method']
		if method != 'X-RAY DIFFRACTION': 				#delete if method not xray
			pdbids.remove(pdbID)
	except:
		print "method for " + pdbID + " is" + "XRAY"
	try:		
		res = d['_refine.ls_d_res_high']	
		if float(res) > 3.0:              				#delete if resolution > 3
			pdbids.remove(pdbID)
	except:
		print "resolution for " + pdbID + "is null"	
		pdbids.remove(pdbID)	
	try:
		missing_res = d['_pdbx_unobs_or_zero_occ_residues.auth_seq_id']  #delete if missing residues 
		if len(set(missing_res)) > 0:
			pdbids.remove(pdbID)
	except:
		print "No missing residues for entry:" + pdbID
	try: 
		missing_atoms = d['_pdbx_unobs_or_zero_occ_atoms.auth_seq_id']   #delete if more than 3 incomplete sidechains 
		num_incomplete_sc = len(set(missing_atoms))
		if num_incomplete_sc > 3:
			pdbids.remove(pdbID)
	except:
		print "No missing atoms for entry:" + pdbID
	mutations = d['_entity.pdbx_mutation']	
	chain_nums = d['_entity_poly.entity_id']
	for i in chain_nums:
		if mutations[int(i)-1] == 'YES':			#delete if there are any mutations
			pdbids.remove(pdbID)					
		else:
			try:
				if int(i) > 0:
					pdbids.remove(pdbID)
			except:
				pass

#a function to extract the text between two substrings (first,last) in a string	(s)								
def find_between( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""			
				
#function to pull ID,name,resolution (a,b,c) from rcsb.org and 
#organize it into a list called 'mainlist'
def fetch(pdbID):
	text1 = 'http://www.rcsb.org/pdb/rest/customReport?pdbids='
	text2 = '&customReportColumns=structureId,resolution,compound,experimentalTechnique,source&service=wsdisplay&format=xml'
	url = text1 + pdbID + text2
	f = urllib2.urlopen(url)
	result = f.read()
	try:
		print result
		res = find_between(result, '<dimStructure.resolution>', '</dimStructure.resolution>')
		name = find_between(result, '<dimEntity.compound>', '</dimEntity.compound>')
		mainlist.append((pdbID, name, res))
	except:
		print "nothing for PDBID:"	+ pdbID
		
#function to return the indices of duplicate items in a list:
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
    
#function to filter redundant proteins from mainlist, 
#keeping only highest res entries for each distinct protein 
def filter_redundant_strc(mainlist):
	blist = []
	for (a,b,c) in mainlist:
		blist.append(b)    					
	d = {}			
	for i in set(blist):
		value = list_duplicates_of(blist, i)	
		d[i] = value	
	clist = []
	for (a,b,c) in mainlist:
		try:
			clist.append(float(c)) 
		except: clist.append(10.0)
	delete = []
	keep = []	
	for key in d.keys():  
		cvals = []
		for x in d[key]:
			newc = clist[x]
			cvals.append(newc) 
		clow = min(cvals)				
		for x in d[key]:  
			newc = clist[x]
			if float(newc) == float(clow): 
				keep.append(x)
			else:  
				delete.append(x)		
	for index in sorted(delete, reverse=True):  
		del mainlist[index]		
	for (a,b,c) in mainlist:
		filteredpdbIDs.append(str(a[0:4]))							
		
#generate a list of the pdbIDs and chains for proteins in the filtered list:				
def get_chains(pdbID):
	d = MMCIF2Dict(pdbID + '.cif')
	chain_ids =  d['_entity_poly.pdbx_strand_id'] 
	for i in set(chain_ids):
		if i != ',':
			outputlist.append(pdbID + str(i))

#string functions together and generate output in folders organized by taxID			
for taxID in taxidlist:
	os.mkdir(str(taxID))
	os.chdir(str(taxID))
	outfilename = str(taxID) + '.txt'
	pdbids = []
	query(taxID)
	initial_num_entries = len(pdbids)
	pdbl = PDBList() 
	cwd = os.getcwd() 
	pdbl.download_pdb_files(pdbids, obsolete=False, pdir=cwd, file_format='mmCif') 
	for pdbID in pdbids:
		try:
			filter_bad_strc(pdbID)
		except: 
			print "No pdb entries for protein: " + str(pdbID)
	mainlist = []
	for pdbID in pdbids:
		fetch(pdbID)
	filteredpdbIDs = []
	filter_redundant_strc(mainlist)
	outputlist = []
	for pdbID in filteredpdbIDs:
		try:
			get_chains(pdbID)
		except:
			print "No pdb entries for protein: " + str(pdbID)
	final_num_entries = len(filteredpdbIDs)	
	if len(outputlist) >=1:	
		print filteredpdbIDs
		ofile = open(outfilename, 'w')
		header = str(final_num_entries) + " structures filtered out of " + str(initial_num_entries) + " initial structures\n"
		ofile.write(header)
		for s in outputlist:
			ofile.write("%s\n" % str(s))
		ofile.close()	
	os.chdir('..')	
	


