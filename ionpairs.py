'''
RETURNS A LIST OF THE RESIDUE NUMBER PAIRS FOR ALL SALT BRIDGES IN A PROTEIN, 
DEFINED AS TWO OPPOSITELY CHARGED ATOMS WITHIN 4 A

TO VISUALIZE SALT BRIDGES IN PYMOL:
select negative, (resn ASP+Glu and name OD*+OE*)
select positive, (resn Lys and name NZ) or (resn arg and name NE+NH*)
distance('saltbridge', 'negative', 'positive', '4.0', '0')
'''

#USAGE:
#ipython ionpairs.py PDBFILE.pdb

from pyrosetta import *
init()
import sys


protein = sys.argv[1]
pose = pose_from_pdb(protein)
nres = pose.total_residue()



#how many charged residues are there in total?
charged = []
for i in range(1,nres+1):
	if pose.residue(i).is_charged() == True:
		charged.append(i)
print "The number of charged residues is:" + str(len(charged))	



		
#make list of res numbers for 4 charged types (RKDE):
lys = []
arg = []
glu = []
asp = []		
for i in range(1, nres+1):
	if pose.residue(i).name() == 'ARG':
		arg.append(i)
	elif pose.residue(i).name() == 'LYS':
		lys.append(i)
	elif pose.residue(i).name() == 'GLU':
		glu.append(i)
	elif pose.residue(i).name() == 'ASP':	#need to add terminal residue names
		asp.append(i)		
	else:
		pass
				

#iterate over RKDE lists and make tuple of residue number pairs in salt bridge, defined by cutoff distance of 4 A:
pairs = []
for i in lys:
	a1 = pose.residue(i).xyz("NZ") 
	for x in glu:
		a2 = pose.residue(x).xyz("OE1") 
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OE2") #counting both glu oxygens as charged
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))
	for x in asp:
		a2 = pose.residue(x).xyz("OD1") #likewise both asp oxygens
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OD2")
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))		
for i in arg:
	a1 = pose.residue(i).xyz("NH1")  
	for x in glu:
		a2 = pose.residue(x).xyz("OE1")
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OE2")
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))	
	for x in asp:
		a2 = pose.residue(x).xyz("OD1")
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OD2")
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))	
	a1 = pose.residue(i).xyz("NH2")  #counting both arg nitrogens as charged 
	for x in glu:
		a2 = pose.residue(x).xyz("OE1")
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OE2")
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))	
	for x in asp:
		a2 = pose.residue(x).xyz("OD1")
		vector = a1 - a2
		a3 = pose.residue(x).xyz("OD2")
		vector2 = a1 - a3
		if vector.norm() <= 4.0 or vector2.norm() <= 4.0:
			pairs.append((i,x))			
			
#eliminate redundancies in pair list; for example if two glu oxygens are within 4 A of a particular lys nitrogen 
#the pair would be counted twice by the above code:
saltbridges = []		
for a,b in pairs:
  if (a,b) not in saltbridges:
    saltbridges.append((a,b))	
			
print "SALT BRIDGES" + str(saltbridges)	
print "the number of ion pairs is:" + str(len(saltbridges))

'''
SOME RANDOM CODE FOR ANALYZING PAIRWISE ENERGIES LATER ON:

In [1]: from pyrosetta import *
In [2]: init()
In [3]: pose = pose_from_pdb('5k8a.clean.pdb')
In [4]: sf = get_fa_scorefxn()
In [6]: emap = pyrosetta.rosetta.core.scoring.EMapVector()
In [7]: res1 = pose.residue(1)
In [8]: res2 = pose.residue(2)
In [9]: sf(pose)
In [10]: sf.eval_ci_2b(res1,res2,pose,emap)
In [11]: print emap

I BELIEVE THIS WORKS TO GET PAIRWISE ENERGY FOR TWO RESIDUES
In [42]: eg = pose.energies().energy_graph()     
In [53]: sf = get_fa_scorefxn()
core.scoring.ScoreFunctionFactory: SCOREFUNCTION: ref2015
In [54]: sf(pose)
Out[54]: -1019.7750140831696
In [55]: print eg.find_energy_edge(1,2).dot(sf.weights()) 
-1.22941876786
AND DOING THIS YOU CAN GET JUST THE FA_ELEC (COULOMBIC) PAIRWISE ENERGY FOR THE TWO
In [46]: sf2 = ScoreFunction()
In [47]: from pyrosetta.rosetta.core.scoring import fa_elec
In [49]: sf2.set_weight(fa_elec, 1.0)
In [50]: sf2(pose)
Out[50]: -2384.6512927566896
In [51]: print eg.find_energy_edge(1,2).dot(sf2.weights()) 
-0.808034744857

TO LOOK AT FA_ELEC TERM FOR SINGLE RES
In [21]: print pose.energies().show(1)


'''



					
			