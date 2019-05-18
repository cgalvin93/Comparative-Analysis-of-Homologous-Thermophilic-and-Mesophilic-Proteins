
import __main__
__main__.pymol_argv = ['pymol','-qc'] # Pymol: quiet and no GUI
from time import sleep
import pymol
pymol.finish_launching()
from pymol import cmd
from pyrosetta import *
init()

dataset = {
'1tyoA,2e0cA':'6c0e-A', 
'2cyaA':'1n3l-A', 
'2yv2A':'6g4q-A',
'2yvuA':'6c6b-B',
'2yzkA':'4rv4-B', 
'4fn4A,2z1nA':['5x8h-A','6b9u-A','5ts3-A','5tt0-A'],       #therms grouped, not all mesos homologues to both
'3ak3A,1wb8A':['5gxo-A','1unf-X'],		
'1geqA,2ekcA':['6dwe-A','1k3u-A'], 				
'1j2pA':['1g65-G','4r3o-S'],                      	
'5l2pA,1jjiA':'4wy5-A', 
'1kr4A,1p1lA':'3opk-C', 
'1t5oA':'2a0u-A', 
'1vhvA':'3i4t-A',
'2f6xA':'3w01-A', 
'3ic4A':'3nzn-A', 
'3mm5A':'2v4j-A', 
'3mm5B':'2xsj-B', 
'3ncrA':'3l7p-E', 
'4eb7A':'5wgb-A',
'1qlmA,4gvqA':'4fio-A', 
'4twjA':['5xhs-A','6flg-B'], 
'1ekeA':'3puf-D', 
'1h72C':'4p52-A', 
'2p3eA,1twiA':'1hkv-A', 
'2hf9A':'4lps-A', 
'2pa6A':['3otr-B','5idz-A','5ohg-B'], 
'1vbfA,2yxeA,1jg1A':'1i1n-A', 
'2yzlA':'1obg-A', 
'3fycA':'1zq9-A', 
'3ixqA':'4nml-A', 
'4rflA':'3ce9-A', 
'4bhdA':['5gvk-A','1eji-A','5v7i-B'], 
'1mjfA':'4yuv-B', 
'1pznA':'1xu4-A', 
'1s4eA':'1wuu-A', 
'2dfiA':'5d6e-A', 
'2jd60':['3bve-A','3vnx-A','5gou-P'], 
'5aovA':'5uog-D', 
'2bwaA':'1oa4-A', 
'4m0kA':'4mb6-A',
'1qezA':'1i40-A', 
'1gehA':['5mz2-D','1tel-B'],
'2zf5Y':'3wxi-A', 
'5nofA':'4n5v-B',
'1nquA':['1ejb-A','2f59-D'], 
'1oy5A':['5d9f-A','4h3z-B'], 
'1tz7A':'1x1n-A', 
'1wwrA':'3dh1-A', 
'2ct8A':'6ax8-A', 
'2egzA':'3l9c-A', 
'2v8pA':['4dxl-A','1oj4-A'], 
'2yvwA':['5u4h-A','3r38-A'],
'2z1mA':'5in4-A', 
'3c9uA':'5cm7-A',
'1fxpA,3e12A':'3und-B', 
'3kb6A':'4cuk-B', 
'3ztoA':['5yih-A','5v6d-F','5iom-A','5go1-A'], 
'3hjnA,5h56A':['4tmk-A','3ld9-A'], 
'5szeA':'5new-A', 
'5tvaA':'5flg-A', 
'1b9bA':['5upr-A','1m6j-A'], 
'1c3uA':'4eei-B', 
'1i4nA':'6bma-A', 
'1kq3A':'1ta9-B', 
'1r3eA':'1k8w-A', 
'1vkyA':'1yy3-A', 
'1vlhA':['1o6b-A','5ts2-A','5h7x-E'], 
'1vm6A':'3qy9-B', 
'1vpeA':'1ltk-C', 
'1worA':'1wsv-A', 
'1zorA':'5yfn-A', 
'2ashA':'5sw3-A', 
'2btyA':'3l86-A', 
'2gtdA':'3djc-B', 
'2o5rA':'6b1p-A', 
'2p3nA':'4as4-A', 
'2w35A':'3goc-A', 
'3a06A':'5kqo-A',
'2z04A,3ax6A':'4ma5-A',  
'3do6A':'5a4j-A', 
'3l0oA':'5jji-C', 
'2hk9A,3u62A':'2egg-B', 
'4gtaA':'4p5b-B', 
'4p6yA':'1vhe-A', 
'4qdnA':'2zyc-A', 
'1rvgA':'3gay-A', 
'2g82A':['5o0v-A','1k3t-A','5jyf-B'], 
'2a8yA':'5tc5-A', 
'2vc7A':'1jgm-A', 
'3f8rA':['5utx-B','4ccr-D'] 
}


#for dictionary entries containing more than one thermophile, splits into list of individual thermophiles
def return_thermos(key):
	tempthermos = []	
	id1 = key[0:5]
	tempthermos.append(id1)
	try:
		id2 = key[6:11]
		if id2 != '':
			tempthermos.append(id2)
	except:
		pass		
	try:
		id3 = key[12:17]
		if id3 != '':
			tempthermos.append(id3)	
	except:
		pass	
	try:
		id4 = key[18:23]
		if id4 != '':
			tempthermos.append(id4)
	except:
		pass	
	try:
		id5 = key[24:29]
		if id5 != '':
			tempthermos.append(id5)							
	except:
		pass	
	return tempthermos
		
#likewise for entries with more than one mesophile			
def return_mesos(key):
	tempmesos = []		
	value = dataset[key]
	crit = len(value[0])
	if crit > 1:
		numids = len(value) 
		for i in value[0:numids]:
			tempmesos.append(i)
	else:
		tempmesos.append(value)
	return tempmesos
	
def return_aligned_res():
	cmd.align("thermo", "meso", object='aln')
	raw_aln = cmd.get_raw_alignment('aln')
	idx2resi = {}
	cmd.iterate('aln', 'idx2resi[model, index] = resi', space={'idx2resi': idx2resi})
	raw_res = []
	for idx1, idx2 in raw_aln:
		raw_res.append((idx2resi[idx1], idx2resi[idx2]))
	aligned_res = []
	for (a,b) in raw_res:
		if (a,b) not in aligned_res:
			aligned_res.append((a,b))
	return aligned_res	

def return_SB(protein, cutoff):
	pose = protein
	nres = pose.total_residue()
	lys = []							#make list of res numbers for 4 charged types (RKDE):
	arg = []
	glu = []
	asp = []		
	for i in range(1, nres+1):
		if pose.residue(i).name() == 'ARG':
			arg.append(i)
		elif pose.residue(i).name() == 'ARG:NtermProteinFull':
			arg.append(i)
		elif pose.residue(i).name() == 'ARG:CtermProteinFull':
			arg.append(i)		
		elif pose.residue(i).name() == 'LYS':
			lys.append(i)
		elif pose.residue(i).name() == 'LYS:NtermProteinFull':
			lys.append(i)
		elif pose.residue(i).name() == 'LYS:CtermProteinFull':
			lys.append(i)	
		elif pose.residue(i).name() == 'GLU':
			glu.append(i)
		elif pose.residue(i).name() == 'GLU:NtermProteinFull':
			glu.append(i)
		elif pose.residue(i).name() == 'GLU:CtermProteinFull':
			glu.append(i)		
		elif pose.residue(i).name() == 'ASP':	
			asp.append(i)	
		elif pose.residue(i).name() == 'ASP:NtermProteinFull':
			asp.append(i)
		elif pose.residue(i).name() == 'ASP:CtermProteinFull':
			asp.append(i)			
		else:
			pass
	pairs = []									#iterate over RKDE lists and make tuple of residue 
	dcut = float(cutoff)
	for i in lys:								
		a1 = pose.residue(i).xyz("NZ") 
		for x in glu:
			a2 = pose.residue(x).xyz("OE1") 
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2") #counting both glu oxygens as charged
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))
		for x in asp:
			a2 = pose.residue(x).xyz("OD1") #likewise both asp oxygens
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))		
	for i in arg:
		a1 = pose.residue(i).xyz("NH1")  
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))	
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))	
		a1 = pose.residue(i).xyz("NH2")  #counting both arg nitrogens as charged 
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))	
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if vector.norm() <= dcut or vector2.norm() <= dcut:
				pairs.append((i,x))			
	saltbridges = []					#eliminate redundant sb in pairs (eg both lys n w/in cutoff from glu o)
	for (a,b) in pairs:
 		if (a,b) not in saltbridges:
   	 		saltbridges.append((a,b))	
   	return saltbridges			
	
results = []	
frac_results = []

for key in dataset.keys():
	thermos = return_thermos(key) 
	mesos = return_mesos(key)
	for thermophile in thermos:
		thermofile = str(thermophile) + '.pdb'
		thermo = pose_from_pdb(thermofile) 											#load thermo to pyrosetta
		cmd.load(thermofile, "thermo")												#load thermo into pymol
		thermo_SB = return_SB(thermo, 4.0)											#create list of thermo salt bridges
		for mesophile in mesos:
			mesofile = str(mesophile) + '.pdb'										
			cmd.load(mesofile,"meso")												#load meso into pymol
			aligned_res = return_aligned_res()										#create list of aligned res between thermo and meso
			cmd.delete("meso")														#delete meso from pymol
			meso = pose_from_pdb(mesofile)											#load meso into pyrosetta
			aligned_res_ros_index = [] 
			thermo_chain = str(thermophile[4])
			meso_chain = str(mesophile[5])
			for (a,b) in aligned_res:											#convert pdb numbering of aligned res to rosetta indices	
				try:
					thermo_index = str(thermo.pdb_info().pdb2pose(thermo_chain,int(a)))	
					meso_index = str(meso.pdb_info().pdb2pose(meso_chain,int(b)))
					thermo_change = thermo_index.replace('L','')
					meso_change = meso_index.replace('L','')
					aligned_res_ros_index.append((thermo_change, meso_change))
				except:
					print "PROBLEM WITH: " + thermofile, mesofile 	
			res_dict = {}															#dictionary of aligned res, key = meso res, value = corresponding thermo res
			for (a,b) in aligned_res_ros_index:
				res_dict[b] = a
			meso_SB = return_SB(meso, 4.0)											#create list of meso salt bridges
			conserved_sb = []
			for (a,b) in meso_SB:													#loop through meso salt bridges, convert res numbers to corresponding thermo res, check if thermo has saltbridge in same position
 				try:
 					res_1 = res_dict[str(a)]
					res_2 = res_dict[str(b)]
					for (c,d) in thermo_SB:
						if int(res_1) == int(c):
							if int(res_2) == int(d):
								conserved_sb.append((a,b,c,d))
				except:
					pass				
			ncsb = float(len(conserved_sb))
			nmsb = float(len(meso_SB))
			frac_meso_sb_conserved = float(ncsb/nmsb)
			s = "The fraction of conserved salt bridges between " + str(thermophile) + " and " + str(mesophile) + " is: " + str(frac_meso_sb_conserved)
			results.append(s)
			frac_results.append(frac_meso_sb_conserved)
		cmd.delete("thermo")														#delete thermo from pymol
		
ofile = open('conservation_results.txt', 'w')

for x in range(len(results)):
	ofile.write(results[x] + '\n')

import scipy
from scipy import stats

a = scipy.array(frac_results)
mean_cons = scipy.mean(a)
var = scipy.var(a)
std = scipy.std(a)
sem = stats.sem(a)
	
r1 = "\nThe mean % of structurally conserved mesophile saltbridges is: " + str(mean_cons); ofile.write(r1 + '\n')
r2 = "standard deviation: " + str(std); ofile.write(r2 + '\n')
r3 = "variance: " + str(var); ofile.write(r3 + '\n')
r4 = "standard error: " + str(sem); ofile.write(r4 + '\n')

ofile.write(str(frac_results))

ofile.close()
					
'''
python
cmd.align('1tyoA', '6c0e-A', object='aln')
raw_aln = cmd.get_raw_alignment('aln')
idx2resi = {}
cmd.iterate('aln', 'idx2resi[model, index] = resi', space={'idx2resi': idx2resi})
for idx1, idx2 in raw_aln:
    print('%s -> %s' % (idx2resi[idx1], idx2resi[idx2]))

python end		


super 
The fraction of conserved salt bridges between 2e0cA and 6c0e-A is: 0.6
The fraction of conserved salt bridges between 5b1yA and 5x8h-A is: 0.0
The fraction of conserved salt bridges between 5b1yA and 6b9u-A is: 0.0769230769231
The fraction of conserved salt bridges between 5b1yA and 5itv-D is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5ts3-A is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5xtg-B is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5tt0-A is: 0.0
The fraction of conserved salt bridges between 1tyoA and 6c0e-A is: 0.25
The fraction of conserved salt bridges between 2e0cA and 6c0e-A is: 0.6

align
The fraction of conserved salt bridges between 2e0cA and 6c0e-A is: 0.6
The fraction of conserved salt bridges between 5b1yA and 5x8h-A is: 0.0
The fraction of conserved salt bridges between 5b1yA and 6b9u-A is: 0.0833333333333
The fraction of conserved salt bridges between 5b1yA and 5itv-D is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5ts3-A is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5xtg-B is: 0.0
The fraction of conserved salt bridges between 5b1yA and 5tt0-A is: 0.0
The fraction of conserved salt bridges between 1tyoA and 6c0e-A is: 0.25
The fraction of conserved salt bridges between 2e0cA and 6c0e-A is: 0.6
'''
			

	

