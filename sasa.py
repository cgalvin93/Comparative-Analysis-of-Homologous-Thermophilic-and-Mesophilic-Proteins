#RETURNS FRACTION OF SURFACE RESIDUES OF PROTEIN AND AVERAGED FRACTION FOR SET OF PROTEINS
#AS DEFINED BY HAVING A RELATIVE SIDECHAIN SOLVENT EXPOSED SURFACE AREA OF GREATER THAN 0.5
#RELATIVE_SASA = SASA / SASA_MAX
#WHERE SASA MAX TAKEN FROM GLY-X-GLY TRIPEPTIDE
#ipython sasa.py sasaresults.txt *.pdb


import sys
from pyrosetta import *
init()

outfilename = sys.argv[1] 
ofile = open(outfilename, 'w') 

from pyrosetta.rosetta.core.scoring.sasa import *

nsurf_list = []
nres_list = []
def report_surface_ratio(filename):
	pose = pose_from_pdb(str(filename))  
	sasa_scores = []
	for float in pyrosetta.rosetta.core.scoring.sasa.rel_per_res_sc_sasa(pose):
		sasa_scores.append(float)
	surface_res = []	
	core_res = []
	for i in sasa_scores:
		if i > 0.5:
			surface_res.append(int(sasa_scores.index(i) + 1))	
		elif i <= 0.5:
			core_res.append(int(sasa_scores.index(i) + 1))
	nsurf = len(surface_res)
	nsurf_list.append(nsurf)
	nres = pose.total_residue()
	nres_list.append(nres)
	result = "\n" + filename + "\nsurface ratio:" + str(nsurf) + "/" + str(nres)
	ofile.write(result)
	
for filename in sys.argv[2:]:
	report_surface_ratio(filename)
	
totalnsurf = sum(nsurf_list)
totalnres = sum(nres_list)	
average = "\nThe averaged fraction of surface residues for the set is:" + str(float(totalnsurf)/float(totalnres))
ofile.write(average)
ofile.close()	
		
		

'''
THIS IS ROSETTAS BUILT IN IS_RES_EXPOSED FUNCTION
does the same thing but much more computationally expensive

for i in surface_res:
	print pyrosetta.rosetta.core.scoring.sasa.is_res_exposed(pose,i)
'''		
		