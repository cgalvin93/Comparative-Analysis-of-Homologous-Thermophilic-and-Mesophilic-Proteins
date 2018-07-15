#script for calculating the number of hydrogen bonds per residue for a set of proteins
#in directory with pdb files of interest, type command:
#ipython hb.py hbresults.txt *.pdb

'''
import sys
from pyrosetta import *
init()
from pyrosetta.rosetta.core.scoring.hbonds import HBondSet
from pyrosetta.toolbox import get_hbonds

outfilename = sys.argv[1] 
ofile = open(outfilename, 'w')  

def report_nhbonds_per_res(pdb_file):  
	pose = pose_from_pdb(pdb_file)
	hbs = pyrosetta.rosetta.core.scoring.hbonds.HBondSet
	hbond_set = get_hbonds(pose)
	nhb = hbs.nhbonds(hbond_set)
	nres = pose.total_residue()
	result = "\nThe number of hydrogen bonds per residue for" + pdb_file + "is:" + str(float(nhb)/float(nres))
	ofile.write(result)

for filename in sys.argv[2:]:
	report_nhbonds_per_res(filename)
	
ofile.close()	


'''
#EXECUTE THIS INSTEAD TO GET NHBONDS/NRES FOR A WHOLE SET, RATHER THAN EACH INDIVIDUAL PROTEIN IN A SET(use same command):

import sys
from pyrosetta import *
init()
from pyrosetta.rosetta.core.scoring.hbonds import HBondSet
from pyrosetta.toolbox import get_hbonds
hbs = pyrosetta.rosetta.core.scoring.hbonds.HBondSet

outfilename = sys.argv[1] 
nhbond_list = []
nres_list = []

for filename in sys.argv[2:]:
	pose = pose_from_pdb(filename)
	hbond_set = get_hbonds(pose)
	nhb = hbs.nhbonds(hbond_set)
	nres = pose.total_residue()
	nhbond_list.append(nhb)
	nres_list.append(nres)
	
totalnhb = sum(nhbond_list)
totalnres = sum(nres_list)

ofile = open(outfilename, 'w') 
result = "\nThe number of hydrogen bonds per residue for the set is:" + str(float(totalnhb)/float(totalnres))
ofile.write(result)
ofile.close()
		
