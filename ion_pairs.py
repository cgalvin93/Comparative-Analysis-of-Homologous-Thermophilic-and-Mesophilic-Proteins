#time ipython ion_pairs.py

'''
dataset = {
'1tyoA,2e0cA':'6c0e-A',
'5b1yA':['5x8h-A','6b9u-A','5itv-D','5ts3-A','5xtg-B','5tt0-A'],
'3e70C,5l3vA,1ls1A,2iylD,5l3wA':['6fqd-B','6cy5-B','1zu5-B']
}


#'1vmaA':'6fqd-B',   
#'3e70C,5l3vA,1ls1A,2iylD,5l3wA':['6fqd-B','6cy5-B','1zu5-B']    #####idk about these, ftsy/signal particle receptor, membrane protein transport




									LARGE DATASET 
									  104 therms, 118 meso
					 RES < 3.0, CORRECT SOURCE ORGANISMS, NO MUTATIONS
					BUT CHAIN LENGTH DIFFERENCES UP TO 50 RES IN SOME CASES
'''
		
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

#a function to take the mean of a list of values since im doing that a lot
def take_mean(list):
	the_sum = float(sum(list))
	elements = float(len(list))
	if elements == 0:
		the_mean = 0.0
	else:
		the_mean = float(the_sum/elements)
	return the_mean
	
#function to identify ion pairs and analyze parameters for each individual protein
def return_SB(protein, cutoff_low, cutoff_high):
	filename = protein + '.pdb'
	pose = pose_from_pdb(filename)
	nres_it = pose.total_residue()
	nres = float(pose.total_residue())
	lys = []; arg = []; glu = []; asp = []							#make list of res numbers for 4 charged types (RKDE):		
	for i in range(1, nres_it+1):         #for all res
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
		elif pose.residue(i).name() == 'ASP':	#need to add terminal residue names
			asp.append(i)	
		elif pose.residue(i).name() == 'ASP:NtermProteinFull':
			asp.append(i)
		elif pose.residue(i).name() == 'ASP:CtermProteinFull':
			asp.append(i)			
		else:
			pass
	pairs = []									#iterate over RKDE lists and make tuple of residue nums for sb pairs
	dcutlow = float(cutoff_low)
	dcuthi = float(cutoff_high)
	for i in lys:								
		a1 = pose.residue(i).xyz("NZ") 
		for x in glu:
			a2 = pose.residue(x).xyz("OE1") 
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2") #counting both glu oxygens as charged
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))
		for x in asp:
			a2 = pose.residue(x).xyz("OD1") #likewise both asp oxygens
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))		
	for i in arg:
		a1 = pose.residue(i).xyz("NH1")  
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))	
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))	
		a1 = pose.residue(i).xyz("NH2")  #counting both arg nitrogens as charged 
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))	
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))	
		a1 = pose.residue(i).xyz("NE")  #3RD ARG NITROGEN
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))	
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				pairs.append((i,x))						
	saltbridges = []					#eliminate redundant sb in pairs (eg both lys n w/in cutoff from glu o)
	for (a,b) in pairs:
 		if (a,b) not in saltbridges:
   	 		saltbridges.append((a,b))
   	anti_pairs = []									#UNFAVORABLE INTERAXNS 
	for i in lys:								
		a1 = pose.residue(i).xyz("NZ") 
		for x in arg:
			a2 = pose.residue(x).xyz("NH1") 
			vector = a1 - a2
			a3 = pose.residue(x).xyz("NH2") #counting both glu oxygens as charged
			vector2 = a1 - a3
			a4 = pose.residue(x).xyz("NE")
			vector3 = a1 - a4
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi or dcutlow < vector3.norm() <= dcuthi:
				anti_pairs.append((i,x))
		for x in lys:
			if i != x:	
				a2 = pose.residue(x).xyz("NZ")
				vector = a1 - a2
				if dcutlow < vector.norm() <= dcuthi:
					anti_pairs.append((i,x))
	for i in glu:
		a1 = pose.residue(i).xyz("OE1")
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				anti_pairs.append((i,x))	
		for x in glu:
			if i != x:
				a2 = pose.residue(x).xyz("OE1")
				vector = a1 - a2
				a3 = pose.residue(x).xyz("OE2")
				vector2 = a1 - a3
				if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
					anti_pairs.append((i,x))			
		a1 = pose.residue(i).xyz("OE2")  
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				anti_pairs.append((i,x))	
		for x in glu:
			if i != x:
				a2 = pose.residue(x).xyz("OE1")
				vector = a1 - a2
				a3 = pose.residue(x).xyz("OE2")
				vector2 = a1 - a3
				if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
					anti_pairs.append((i,x))					
	saltbridges = []
	for (a,b) in pairs:
		if (a,b) not in saltbridges:
			saltbridges.append((a,b))		
   	anti_pairs = []									#UNFAVORABLE INTERAXNS 
	for i in lys:								
		a1 = pose.residue(i).xyz("NZ") 
		for x in arg:
			a2 = pose.residue(x).xyz("NH1") 
			vector = a1 - a2
			a3 = pose.residue(x).xyz("NH2") #counting both glu oxygens as charged
			vector2 = a1 - a3
			a4 = pose.residue(x).xyz("NE")
			vector3 = a1 - a4
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi or dcutlow < vector3.norm() <= dcuthi:
				anti_pairs.append((i,x))
		for x in lys:
			if i != x:	
				a2 = pose.residue(x).xyz("NZ")
				vector = a1 - a2
				if dcutlow < vector.norm() <= dcuthi:
					anti_pairs.append((i,x))
	for i in glu:
		a1 = pose.residue(i).xyz("OE1")
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				anti_pairs.append((i,x))	
		for x in glu:
			if i != x:
				a2 = pose.residue(x).xyz("OE1")
				vector = a1 - a2
				a3 = pose.residue(x).xyz("OE2")
				vector2 = a1 - a3
				if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
					anti_pairs.append((i,x))			
		a1 = pose.residue(i).xyz("OE2")  
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				anti_pairs.append((i,x))	
		for x in glu:
			if i != x:
				a2 = pose.residue(x).xyz("OE1")
				vector = a1 - a2
				a3 = pose.residue(x).xyz("OE2")
				vector2 = a1 - a3
				if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
					anti_pairs.append((i,x))	
	antiSB = []					
	for (a,b) in anti_pairs:
 		if (a,b) not in antiSB:
   	 		antiSB.append((a,b))
   	n_unfavorable = float(len(antiSB))		 		#total numher unfavorable interaxns	
   	nsb = float(len(saltbridges))			#total number of salt bridges
	ares = []									#number of branched residues
	bres = []
	allres = []
	for a,b in saltbridges:
		ares.append(a)
		bres.append(b)
	for res in ares:
		allres.append(res)
	for res in bres:
		allres.append(res)
	unique_sb_res = []
	for res in allres:
		if res not in unique_sb_res:
			unique_sb_res.append(res)
	branched_res = []		
	for res in unique_sb_res:
		count = []
		for a,b in saltbridges:
			if a == res:
				count.append(a)
			if b == res:
				count.append(b)
		ninteraxns = len(count)
		if ninteraxns > 1:
			branched_res.append(pose.residue(res).name())
	n_branched_res = len(branched_res)				#fraction sb res in more than one sb
	n_sb_res = float(len(unique_sb_res))
	if n_sb_res > 0:
		n_branched_per_sb_res = float(n_branched_res/n_sb_res)				#fraction branched
	else:
		n_branched_per_sb_res = 0.0
	if nsb>0:
		ratio_fav_unfav = float(n_unfavorable/nsb) 				#ratio unfavorable to fav interaxn
	else:
		ratio_fav_unfav = 0.0
	n_arg = len(arg); n_lys = len(lys); n_glu = len(glu); n_asp = len(asp)	
	n_pos = float(len(arg) + len(lys))
	n_neg = float(len(glu) + len(asp))
	qpqn = float(n_neg/n_pos)	
	n_charged_res = float(len(arg) + len(lys) + len(glu) + len(asp))	
	n_iso = float(n_charged_res - n_sb_res)
	frac_iso = float(n_iso/n_charged_res)
	#perc_arg = float(n_arg/nres); perc_lys = float(n_lys/nres);perc_glu = float(n_glu/nres);perc_asp = float(n_asp/nres)		#for seq stats on all res
	#res_fracs = (perc_arg,perc_lys,perc_glu,perc_asp)
	return nsb, nres, n_branched_per_sb_res, ratio_fav_unfav, frac_iso, qpqn  #res_fracs,



    


########################################## loop through data dictionary, analyze and compare results within each family
import texttable as tt
from pyrosetta import *
init()
from pyrosetta.toolbox import get_secstruct
from pyrosetta.rosetta.core.scoring.sasa import *
ofile = open('mono05.txt', 'w')
avg_all_therm = []; avg_all_meso = []					#lists to hold averaged values for each parameter from each protein family
frac_avg_therm = []; frac_avg_meso = []
percds = []
avg_thermo_nbranched = []; avg_meso_nbranched = []
avg_thermo_ratios = []; avg_meso_ratios = []
avg_thermo_frac_iso = []; avg_meso_frac_iso = []
#avg_thermo_res_fracs = []; avg_meso_res_fracs = []
avg_thermo_nq = []; avg_meso_nq = []
avg_thermo_qpqn = []; avg_meso_qpqn = []
the_keys = []
greater_nsb = []
greater_branching = []
smaller_ratio = []
less_iso = []
#higher_lys = []
#higher_glu = []
#less_asp = []
#higher_arg = []
higher_qpqn = []
for key in dataset.keys():
	the_keys.append(key)
	thermos = return_thermos(key)
	mesos = return_mesos(key)
	thermo_nsb = []; meso_nsb = []
	thermfracnsb = []; mesfracnsb = []
	thermfracnres = []; mesfracnres = []
	thermo_n_branched = []; meso_n_branched = []
	thermo_ratios = []; meso_ratios = []
	thermo_frac_iso = []; meso_frac_iso = []
	#thermo_res_fracs = []; meso_res_fracs = []
	thermo_qpqn = []; meso_qpqn = []
	for ptn in thermos:
		my_nsb, my_nres, n_branched_res, ratio_fav_unfav, frac_iso, qpqn  = return_SB(ptn, 0.0, 5.0) 
		nsb_per_res = float(my_nsb/my_nres)	
		thermo_nsb.append(nsb_per_res)	
		thermfracnsb.append(my_nsb)
		thermfracnres.append(my_nres)
		thermo_n_branched.append(n_branched_res)
		thermo_ratios.append(ratio_fav_unfav)
		thermo_frac_iso.append(frac_iso)
		thermo_qpqn.append(qpqn)
		#thermo_res_fracs.append(res_fracs)
	for ptn in mesos:
		my_nsb, my_nres, n_branched_res, ratio_fav_unfav, frac_iso, qpqn = return_SB(ptn, 0.0, 5.0) 
		nsb_per_res = float(my_nsb/my_nres)	
		meso_nsb.append(nsb_per_res)	
		mesfracnsb.append(my_nsb)
		mesfracnres.append(my_nres)
		meso_n_branched.append(n_branched_res)
		meso_ratios.append(ratio_fav_unfav)
		meso_frac_iso.append(frac_iso)
		#meso_res_fracs.append(res_fracs)
		meso_qpqn.append(qpqn)
	avg_therm_nsb = take_mean(thermo_nsb); avg_meso_nsb = take_mean(meso_nsb)
	if avg_therm_nsb > avg_meso_nsb:
		greater_nsb.append(avg_therm_nsb)		
	avg_all_therm.append(avg_therm_nsb)										#decimal avg nsb/res
	avg_all_meso.append(avg_meso_nsb)
	mean_thermo_n_branched = take_mean(thermo_n_branched)  #branched res
	mean_meso_n_branched = take_mean(meso_n_branched)
	if mean_thermo_n_branched > mean_meso_n_branched:
		greater_branching.append(mean_thermo_n_branched)
	avg_thermo_nbranched.append(mean_thermo_n_branched); avg_meso_nbranched.append(mean_meso_n_branched)
	mean_thermo_ratio = take_mean(thermo_ratios)			#fraction unfav/fav charge interactions
	mean_meso_ratio = take_mean(meso_ratios)
	if mean_thermo_ratio < mean_meso_ratio:
		smaller_ratio.append(mean_thermo_ratio)
	avg_thermo_ratios.append(mean_thermo_ratio); avg_meso_ratios.append(mean_meso_ratio)
	mean_thermo_frac_iso = take_mean(thermo_frac_iso); mean_meso_frac_iso = take_mean(meso_frac_iso)  #fraction of charges that are isolated (not in sb)
	avg_thermo_frac_iso.append(mean_thermo_frac_iso); avg_meso_frac_iso.append(mean_meso_frac_iso)
	if mean_thermo_frac_iso < mean_meso_frac_iso:
		less_iso.append(mean_thermo_frac_iso)
	therm_avg_qpqn = take_mean(thermo_qpqn); meso_avg_qpqn = take_mean(meso_qpqn)
	avg_thermo_qpqn.append(therm_avg_qpqn); avg_meso_qpqn.append(meso_avg_qpqn)
	if therm_avg_qpqn > meso_avg_qpqn:
		higher_qpqn.append(therm_avg_qpqn)
'''	
	thermfracarg = [];thermfracglu=[];thermfraclys=[];thermfracasp=[]
	for (a,b,c,d) in thermo_res_fracs:					#fraction of each charged residue making up sb network (n_that_res/n_sb_res)
		thermfracarg.append(a)
		thermfraclys.append(b)
		thermfracglu.append(c)
		thermfracasp.append(d)
	therm_avg_arg = take_mean(thermfracarg);therm_avg_lys = take_mean(thermfraclys);therm_avg_glu = take_mean(thermfracglu);therm_avg_asp = take_mean(thermfracasp)	
	avg_thermo_res_fracs.append((therm_avg_arg,therm_avg_lys,therm_avg_glu,therm_avg_asp))
	mesofracarg = [];mesofracglu=[];mesofraclys=[];mesofracasp=[]
	for (a,b,c,d) in meso_res_fracs:
		mesofracarg.append(a)
		mesofraclys.append(b)
		mesofracglu.append(c)
		mesofracasp.append(d)
	meso_avg_arg = take_mean(mesofracarg);meso_avg_lys = take_mean(mesofraclys);meso_avg_glu = take_mean(mesofracglu);meso_avg_asp = take_mean(mesofracasp)	
	avg_meso_res_fracs.append((meso_avg_arg,meso_avg_lys,meso_avg_glu,meso_avg_asp))
	if therm_avg_lys > meso_avg_lys:
		higher_lys.append(therm_avg_lys)
	if therm_avg_glu > meso_avg_glu:
		higher_glu.append(therm_avg_glu)	
	if therm_avg_asp < meso_avg_asp:
		less_asp.append(therm_avg_asp)
	if therm_avg_arg > meso_avg_arg:
		higher_arg.append(therm_avg_arg)
'''		
		


				
	
	
#################################   write overall avgs to outfile with statistical analysis
import scipy
from scipy import stats

n_families = len(the_keys)
n_greater_nsb = len(greater_nsb)
n_greater_branching = len(greater_branching)
n_smaller_ratio = len(smaller_ratio)	
n_less_iso = len(less_iso)
#n_higher_lys = len(higher_lys)
#n_higher_glu = len(higher_glu)
#n_higher_arg = len(higher_arg)
#n_lower_asp = len(less_asp)
n_higher_qpqn = len(higher_qpqn)




ofile.write('\n')		
therm_nsb_array = scipy.array(avg_all_therm)    #avg nsb/res
meso_nsb_array = scipy.array(avg_all_meso)
therm_nsb_mean = scipy.mean(therm_nsb_array)
therm_nsb_var = scipy.var(therm_nsb_array)
therm_nsb_std = scipy.std(therm_nsb_array)
therm_nsb_sem = stats.sem(therm_nsb_array)
meso_nsb_mean = scipy.mean(meso_nsb_array)
meso_nsb_var = scipy.var(meso_nsb_array)
meso_nsb_std = scipy.std(meso_nsb_array)
meso_nsb_sem = stats.sem(meso_nsb_array)
nsb_tstat = stats.ttest_ind(therm_nsb_array,meso_nsb_array)[0] 
nsb_pvalue = stats.ttest_ind(therm_nsb_array,meso_nsb_array)[1]
overall_nsb = "\nTHE AVG NSB/NRES FOR THERMOPHILES IS: " + str(therm_nsb_mean) + " WITH STANDARD DEVIATION: " + str(therm_nsb_std) + ", VARIANCE: " +  str(therm_nsb_var) + " AND STANDARD ERROR: " + str(therm_nsb_sem) + "\nTHE AVG NSB/NRES FOR MESOPHILES IS: " + str(meso_nsb_mean) + " WITH STANDARD DEVIATION: " + str(meso_nsb_std) + ", VARIANCE: " + str(meso_nsb_var) + " AND STANDARD ERROR : " + str(meso_nsb_sem) + "\nTHE T STATISTIC IS: " + str(nsb_tstat) + " AND THE P VALUE IS: " + str(nsb_pvalue)
ofile.write(overall_nsb)
n_fam_observed = "\nTHE NSB/NRES INCREASED IN " + str(n_greater_nsb) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)



ofile.write('\n')
therm_nbr_array = scipy.array(avg_thermo_nbranched)    #avg nbranched res
meso_nbr_array = scipy.array(avg_meso_nbranched)
therm_nbr_mean = scipy.mean(therm_nbr_array)
therm_nbr_var = scipy.var(therm_nbr_array)
therm_nbr_std = scipy.std(therm_nbr_array)
therm_nbr_sem = stats.sem(therm_nbr_array)
meso_nbr_mean = scipy.mean(meso_nbr_array)
meso_nbr_var = scipy.var(meso_nbr_array)
meso_nbr_std = scipy.std(meso_nbr_array)
meso_nbr_sem = stats.sem(meso_nbr_array)
nbr_tstat = stats.ttest_ind(therm_nbr_array,meso_nbr_array)[0] 
nbr_pvalue = stats.ttest_ind(therm_nbr_array,meso_nbr_array)[1]
overall_nbr = "\nTHE AVG FRACTION BRANCHED SB RES FOR THERMOPHILES IS: " + str(therm_nbr_mean) + " WITH STANDARD DEVIATION: " + str(therm_nbr_std) + ", VARIANCE: " + str(therm_nbr_var) + " AND STANDARD ERROR: " + str(therm_nbr_sem) + "\nTHE AVG FRACTION BRANCHED SB RES FOR MESOPHILES IS: " + str(meso_nbr_mean) + " WITH STANDARD DEVIATION: " + str(meso_nbr_std) + ", VARIANCE: " + str(meso_nbr_var) + " AND STANDARD ERROR: " + str(meso_nbr_sem) + "\nTHE T STATISTIC IS: " + str(nbr_tstat) + " AND THE P VALUE IS: " + str(nbr_pvalue)
ofile.write(overall_nbr)
n_fam_observed = "\nTHE FRAC BRANCHED INCREASED IN " + str(n_greater_branching) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)
	


ofile.write('\n')		
therm_ratio_array = scipy.array(avg_thermo_ratios)    #avg ratio fav/unfav q interaxns
meso_ratio_array = scipy.array(avg_meso_ratios)
therm_ratio_mean = scipy.mean(therm_ratio_array)
therm_ratio_var = scipy.var(therm_ratio_array)
therm_ratio_std = scipy.std(therm_ratio_array)
therm_ratio_sem = stats.sem(therm_ratio_array)
meso_ratio_mean = scipy.mean(meso_ratio_array)
meso_ratio_var = scipy.var(meso_ratio_array)
meso_ratio_std = scipy.std(meso_ratio_array)
meso_ratio_sem = stats.sem(meso_ratio_array)
ratio_tstat = stats.ttest_ind(therm_ratio_array,meso_ratio_array)[0] 
ratio_pvalue = stats.ttest_ind(therm_ratio_array,meso_ratio_array)[1]
overall_ratio = "\nTHE AVG N_UNFAVORABLE/NSB FOR THERMOPHILES IS: " + str(therm_ratio_mean) + " WITH STANDARD DEVIATION: " + str(therm_ratio_std) + ", VARIANCE: " +  str(therm_ratio_var) + " AND STANDARD ERROR: " + str(therm_ratio_sem) + "\nTHE AVG N_UNFAVORABLE/NSB FOR MESOPHILES IS: " + str(meso_ratio_mean) + " WITH STANDARD DEVIATION: " + str(meso_ratio_std) + ", VARIANCE: " + str(meso_ratio_var) + " AND STANDARD ERROR : " + str(meso_ratio_sem) + "\nTHE T STATISTIC IS: " + str(ratio_tstat) + " AND THE P VALUE IS: " + str(ratio_pvalue)
ofile.write(overall_ratio)
n_fam_observed = "\nTHE RATIO UNFAV/FAV DECREASED IN " + str(n_smaller_ratio) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)


ofile.write('\n')		
therm_iso_array = scipy.array(avg_thermo_frac_iso)    #avg fraction of isolated charges
meso_iso_array = scipy.array(avg_meso_frac_iso)
therm_iso_mean = scipy.mean(therm_iso_array)
therm_iso_var = scipy.var(therm_iso_array)
therm_iso_std = scipy.std(therm_iso_array)
therm_iso_sem = stats.sem(therm_iso_array)
meso_iso_mean = scipy.mean(meso_iso_array)
meso_iso_var = scipy.var(meso_iso_array)
meso_iso_std = scipy.std(meso_iso_array)
meso_iso_sem = stats.sem(meso_iso_array)
iso_tstat = stats.ttest_ind(therm_iso_array,meso_iso_array)[0] 
iso_pvalue = stats.ttest_ind(therm_iso_array,meso_iso_array)[1]
overall_iso = "\nTHE AVG FRACTION OF ISOLATED CHARGES FOR THERMOPHILES IS: " + str(therm_iso_mean) + " WITH STANDARD DEVIATION: " + str(therm_iso_std) + ", VARIANCE: " +  str(therm_iso_var) + " AND STANDARD ERROR: " + str(therm_iso_sem) + "\nTHE AVG FRACTION OF ISOLATED CHARGES FOR MESOPHILES IS: " + str(meso_iso_mean) + " WITH STANDARD DEVIATION: " + str(meso_iso_std) + ", VARIANCE: " + str(meso_iso_var) + " AND STANDARD ERROR : " + str(meso_iso_sem) + "\nTHE T STATISTIC IS: " + str(iso_tstat) + " AND THE P VALUE IS: " + str(iso_pvalue)
ofile.write(overall_iso)
n_fam_observed = "\nTHE FRAC ISO Q DECREASED IN " + str(n_less_iso) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

ofile.write('\n')		
therm_pn_array = scipy.array(avg_thermo_qpqn)    #avg qp/qn
meso_pn_array = scipy.array(avg_meso_qpqn)
therm_pn_mean = scipy.mean(therm_pn_array)
therm_pn_var = scipy.var(therm_pn_array)
therm_pn_std = scipy.std(therm_pn_array)
therm_pn_sem = stats.sem(therm_pn_array)
meso_pn_mean = scipy.mean(meso_pn_array)
meso_pn_var = scipy.var(meso_pn_array)
meso_pn_std = scipy.std(meso_pn_array)
meso_pn_sem = stats.sem(meso_pn_array)
pn_tstat = stats.ttest_ind(therm_pn_array,meso_pn_array)[0] 
pn_pvalue = stats.ttest_ind(therm_pn_array,meso_pn_array)[1]
overall_pn = "\nTHErmo qnqp: " + str(therm_pn_mean) + " WITH STANDARD DEVIATION: " + str(therm_pn_std) + ", VARIANCE: " +  str(therm_pn_var) + " AND STANDARD ERROR: " + str(therm_pn_sem) + "\nTHE meso qnqp: " + str(meso_pn_mean) + " WITH STANDARD DEVIATION: " + str(meso_pn_std) + ", VARIANCE: " + str(meso_pn_var) + " AND STANDARD ERROR : " + str(meso_pn_sem) + "\nTHE T STATISTIC IS: " + str(pn_tstat) + " AND THE P VALUE IS: " + str(pn_pvalue)
ofile.write(overall_pn)
n_fam_observed = "\nTHE qnqp increaseD IN " + str(n_higher_qpqn) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

'''
ofile.write('\n')		
therm_d_array = scipy.array(avg_thermo_dist)    #avg ion pair distance
meso_d_array = scipy.array(avg_meso_dist)
therm_d_mean = scipy.mean(therm_d_array)
therm_d_var = scipy.var(therm_d_array)
therm_d_std = scipy.std(therm_d_array)
therm_d_sem = stats.sem(therm_d_array)
meso_d_mean = scipy.mean(meso_d_array)
meso_d_var = scipy.var(meso_d_array)
meso_d_std = scipy.std(meso_d_array)
meso_d_sem = stats.sem(meso_d_array)
d_tstat = stats.ttest_ind(therm_d_array,meso_d_array)[0] 
d_pvalue = stats.ttest_ind(therm_d_array,meso_d_array)[1]
overall_d = "\nTHErmo dist: " + str(therm_d_mean) + " WITH STANDARD DEVIATION: " + str(therm_d_std) + ", VARIANCE: " +  str(therm_d_var) + " AND STANDARD ERROR: " + str(therm_d_sem) + "\nTHE meso dist: " + str(meso_d_mean) + " WITH STANDARD DEVIATION: " + str(meso_d_std) + ", VARIANCE: " + str(meso_d_var) + " AND STANDARD ERROR : " + str(meso_d_sem) + "\nTHE T STATISTIC IS: " + str(d_tstat) + " AND THE P VALUE IS: " + str(d_pvalue)
ofile.write(overall_d)
n_fam_observed = "\nTHE dist decreased IN " + str(n_lower_dist) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)
'''
'''
ofile.write('\n')		
therm_res_array = scipy.array(avg_thermo_res_fracs)    #avg residue preferences for salt bridge residues
meso_res_array = scipy.array(avg_meso_res_fracs)
thermo_mean_arg = scipy.mean(therm_res_array,axis=0)[0]
thermo_mean_lys = scipy.mean(therm_res_array,axis=0)[1]
thermo_mean_glu = scipy.mean(therm_res_array,axis=0)[2]
thermo_mean_asp = scipy.mean(therm_res_array,axis=0)[3]
meso_mean_arg = scipy.mean(meso_res_array,axis=0)[0]
meso_mean_lys = scipy.mean(meso_res_array,axis=0)[1]
meso_mean_glu = scipy.mean(meso_res_array,axis=0)[2]
meso_mean_asp = scipy.mean(meso_res_array,axis=0)[3]
thermo_var_arg = scipy.var(therm_res_array,axis=0)[0]
thermo_var_lys = scipy.var(therm_res_array,axis=0)[1]
thermo_var_glu = scipy.var(therm_res_array,axis=0)[2]
thermo_var_asp = scipy.var(therm_res_array,axis=0)[3]
meso_var_arg = scipy.var(meso_res_array,axis=0)[0]
meso_var_lys = scipy.var(meso_res_array,axis=0)[1]
meso_var_glu = scipy.var(meso_res_array,axis=0)[2]
meso_var_asp = scipy.var(meso_res_array,axis=0)[3]
thermo_std_arg = scipy.std(therm_res_array,axis=0)[0]
thermo_std_lys = scipy.std(therm_res_array,axis=0)[1]
thermo_std_glu = scipy.std(therm_res_array,axis=0)[2]
thermo_std_asp = scipy.std(therm_res_array,axis=0)[3]
meso_std_arg = scipy.std(meso_res_array,axis=0)[0]
meso_std_lys = scipy.std(meso_res_array,axis=0)[1]
meso_std_glu = scipy.std(meso_res_array,axis=0)[2]
meso_std_asp = scipy.std(meso_res_array,axis=0)[3]
thermo_sem_arg = stats.sem(therm_res_array,axis=0)[0]
thermo_sem_lys = stats.sem(therm_res_array,axis=0)[1]
thermo_sem_glu = stats.sem(therm_res_array,axis=0)[2]
thermo_sem_asp = stats.sem(therm_res_array,axis=0)[3]
meso_sem_arg = stats.sem(meso_res_array,axis=0)[0]
meso_sem_lys = stats.sem(meso_res_array,axis=0)[1]
meso_sem_glu = stats.sem(meso_res_array,axis=0)[2]
meso_sem_asp = stats.sem(meso_res_array,axis=0)[3]
res_p_values = stats.ttest_ind(therm_res_array,meso_res_array,axis=0)[1] 
arg_pvalue = res_p_values[0]
lys_pvalue = res_p_values[1]
glu_pvalue = res_p_values[2]
asp_pvalue = res_p_values[3]

ofile.write('\n')
thermo_arg_result = "\nTHE AVERAGE FRACTION OF ARGININES in thermophiles (these stats for all res)S: " + str(thermo_mean_arg) + " WITH STANDARD DEVIATION: " + str(thermo_std_arg) + " , VARIANCE: " + str(thermo_var_arg) + " AND STANDARD ERROR: " + str(thermo_sem_arg)
meso_arg_result = "THE AVERAGE FRACTION OF ARGININES COMPOSING MESOPHILIC SALTBIRGDES IS: " + str(meso_mean_arg) + " WITH STANDARD DEVIATION: " + str(meso_std_arg) + " , VARIANCE: " + str(meso_var_arg) + " AND STANDARD ERROR: " + str(meso_sem_arg)
arg_pval = "THE P VALUE IS: " + str(arg_pvalue)
arg_result = thermo_arg_result + '\n' + meso_arg_result + '\n' + arg_pval
ofile.write(arg_result)
n_fam_observed = "\nTHE FRAC arg INCREASED IN " + str(n_higher_arg) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

ofile.write('\n')
thermo_lys_result = "\nTHE AVERAGE FRACTION OF LYSINES COMPOSING THERMOPHILIC SALTBIRGDES IS: " + str(thermo_mean_lys) + " WITH STANDARD DEVIATION: " + str(thermo_std_lys) + " , VARIANCE: " + str(thermo_var_lys)+ " AND STANDARD ERROR: " + str(thermo_sem_lys)
meso_lys_result = "THE AVERAGE FRACTION OF LYSINES COMPOSING MESOPHILIC SALTBIRGDES IS: " + str(meso_mean_lys) + " WITH STANDARD DEVIATION: " + str(meso_std_lys) + " , VARIANCE: " + str(meso_var_lys) +" AND STANDARD ERROR: " + str(meso_sem_lys)
lys_pval = "THE P VALUE IS: " + str(lys_pvalue)
lys_result = thermo_lys_result + '\n' + meso_lys_result + '\n' + lys_pval
ofile.write(lys_result)
n_fam_observed = "\nTHE FRAC LYS INCREASED IN " + str(n_higher_lys) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

ofile.write('\n')
thermo_glu_result = "\nTHE AVERAGE FRACTION OF GLUTAMATES COMPOSING THERMOPHILIC SALTBIRGDES IS: " + str(thermo_mean_glu) + " WITH STANDARD DEVIATION: " + str(thermo_std_glu) + " , VARIANCE: " + str(thermo_var_glu)+ " AND STANDARD ERROR: " + str(thermo_sem_glu)
meso_glu_result = "THE AVERAGE FRACTION OF GLUTAMATES COMPOSING MESOPHILIC SALTBIRGDES IS: " + str(meso_mean_glu) + " WITH STANDARD DEVIATION: " + str(meso_std_glu) + " , VARIANCE: " + str(meso_var_glu)+ " AND STANDARD ERROR: " + str(meso_sem_glu)
glu_pval = "THE P VALUE IS: " + str(glu_pvalue)
glu_result = thermo_glu_result + '\n' + meso_glu_result + '\n' + glu_pval
ofile.write(glu_result)
n_fam_observed = "\nTHE FRAC GLU IN " + str(n_higher_glu) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

ofile.write('\n')
thermo_asp_result = "\nTHE AVERAGE FRACTION OF ASPARTATES COMPOSING THERMOPHILIC SALTBIRGDES IS: " + str(thermo_mean_asp) + " WITH STANDARD DEVIATION: " + str(thermo_std_asp) + " , VARIANCE: " + str(thermo_var_asp)+ " AND STANDARD ERROR: " + str(thermo_sem_asp)
meso_asp_result = "THE AVERAGE FRACTION OF ASPARTATES COMPOSING MESOPHILIC SALTBIRGDES IS: " + str(meso_mean_asp) + " WITH STANDARD DEVIATION: " + str(meso_std_asp) + " , VARIANCE: " + str(meso_var_asp)+ " AND STANDARD ERROR: " + str(meso_sem_asp)
asp_pval = "THE P VALUE IS: " + str(asp_pvalue)
asp_result = thermo_asp_result + '\n' + meso_asp_result + '\n' + asp_pval
ofile.write(asp_result)
n_fam_observed = "\nTHE FRAC asp decreased IN " + str(n_lower_asp) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)
'''
ofile.write('\n')
nsbdata = "\nDATA FOR NSB/NRES: " + "\nTHERMOPHILES = " + str(avg_all_therm) + "\nMESOPHILES = " + str(avg_all_meso)
ofile.write(nsbdata)


ofile.write('\n')
nbrdata = "\nDATA FOR N BRANCHED: " + "\nTHERMOPHILES = " + str(avg_thermo_nbranched) + "\nMESOPHILES = " + str(avg_meso_nbranched)
ofile.write(nbrdata)

ofile.write('\n')
ratiodata = "\nDATA FOR RATIO FAV/UNFAV: " + "\nTHERMOPHILES = " + str(avg_thermo_ratios) + "\nMESOPHILES = " + str(avg_meso_ratios)
ofile.write(ratiodata)


ofile.write('\n')
isodata = "\nDATA FOR FRAC ISO: " + "\nTHERMOPHILES = " + str(avg_thermo_frac_iso) + "\nMESOPHILES = " + str(avg_meso_frac_iso)
ofile.write(isodata)

'''
ofile.write('\n')
resdata = "\nDATA FOR RES PREFERENCES IN SB: " + "\nTHERMOPHILES = " + str(avg_thermo_res_fracs) + "\nMESOPHILES = " + str(avg_meso_res_fracs)
ofile.write(resdata)
'''

ofile.write('\n')
qpqndata = "\nDATA FOR qpqn: " + "\nTHERMOPHILES = " + str(avg_thermo_qpqn) + "\nMESOPHILES = " + str(avg_meso_qpqn)
ofile.write(qpqndata)

'''
ofile.write('\n')
distdata = "\nDATA FOR dist: " + "\nTHERMOPHILES = " + str(avg_thermo_dist) + "\nMESOPHILES = " + str(avg_meso_dist)
ofile.write(distdata)
'''

ofile.close()	