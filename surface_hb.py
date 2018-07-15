# ipython surface_hb.py surfacehb.txt

#init/imports:
from pyrosetta import *
init()
from pyrosetta.rosetta.core.scoring.sasa import *
from pyrosetta.rosetta.core.scoring.hbonds import HBondSet
from pyrosetta.toolbox import get_hbonds

pose = pose_from_pdb('spadc.clean.pdb')


#create a list of the rosetta residue numbers for all surface residues in the protein:
sasa_scores = []
for float in pyrosetta.rosetta.core.scoring.sasa.rel_per_res_sc_sasa(pose):
	sasa_scores.append(float)
surface_res = []
for i in sasa_scores:
	if i > 0.5:
		surface_res.append(int(sasa_scores.index(i) + 1))	
		
print surface_res
		
#return hbond info on surface residues:			
hbs = pyrosetta.rosetta.core.scoring.hbonds.HBondSet
set = get_hbonds(pose)		
for i in surface_res:
	hbs.show(set, pose, i)

		
