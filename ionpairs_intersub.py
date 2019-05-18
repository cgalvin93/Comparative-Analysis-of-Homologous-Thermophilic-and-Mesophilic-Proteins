#ipython compare_SB_complexes.py

#dataset for testing
'''
dataset = {
'4m0k':'4mb6',
'1vlh':['5ts2','5h7x'],
'5l2p':'4wy5',
'4fn4':['5x8h','5ts3','5tt0']
}



					#COMPLEX DATA SET

'''		
dataset = {							
'4m0k':'4mb6',
'2p3n':'4as4',
'1mjf':'4yuv',
'2a8y':'5tc5',
'3ak3':'5gxo',
'1qez':'1i40',
'1vlh':['5ts2','5h7x'],
'2yzk':'4rv4',
'1t5o':'2a0u',
'1b9b':['5upr','1m6j'],
'5l2p':'4wy5',
'3f8r':['5utx','4ccr'],
'3a06':'5kqo',
'2ash':'5sw3',
'2yvu':'6c6b',
'1vm6':'3qy9',
'2z04,3ax6':'4ma5',
'2pa6':['3otr','5idz'],
'1wwr':'3dh1',
'2w35':'3goc',
'1rvg':'3gay',
'1geh':'1tel',
'1c3u':'4eei',
'3kb6':'4cuk',
'2p3e,1twi':'1hkv',
'4rfl':'3ce9',
'4gta':'4p5b',
'2z1m':'5in4',
'2gtd':'3djc',
'5sze':'5new',
'1fxp,3e12':'3und',
'5aov':'5uog',
'3ncr':'3l7p',
'2zf5':'3wxi',
'1h72':'4p52',
'3zto':['5yih','5v6d','5iom','5go1'],
'1oy5':['5d9f','4h3z'],
'3hjn,5h56':'3ld9',
'2g82':['5o0v','1k3t','5jyf'],
'1kr4':'3opk',
'1qlm,4gvq':'4fio',
'3c9u':'5cm7',
'2f6x':'3w01',
'2jd6':['3bve','3vnx'],
'1vhv':'3i4t',
'4bhd':['5gvk','1eji','5v7i'],
'3do6':'5a4j',
'4fn4':['5x8h','5ts3','5tt0'],
'3l0o':'5jji',
'1zor':'5yfn',
'2cya':'1n3l',
'2vc7':'1jgm'		
}


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

def return_thermos(key):
	tempthermos = []	
	id1 = key[0:4]
	tempthermos.append(id1)
	try:
		id2 = key[5:9]
		if id2 != '':
			tempthermos.append(id2)
	except:
		pass		
	return tempthermos	

#a function to take the mean of a list of values since im doing that a lot
def take_mean(list):
	the_sum = float(sum(list))
	elements = float(len(list))
	the_mean = float(the_sum/elements)
	return the_mean
	
#function to identify ion pairs and analyze parameters for each individual protein
def return_SB(protein, cutoff_low, cutoff_high):
	filename = protein + '.pdb1'
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
	sb = []					#eliminate redundant sb in pairs (eg both lys n w/in cutoff from glu o)
	for (a,b) in pairs:
 		if (a,b) not in sb:
   	 		sb.append((a,b))
   	saltbridges = []		
   	for (a,b) in sb:
   		chain1 = pose.pdb_info().chain(a)
   		chain2 = pose.pdb_info().chain(b)
   		if chain1 != chain2:
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
	n_pos = float(len(arg) + len(lys))
	n_neg = float(len(glu) + len(asp))
	qpqn = float(n_neg/n_pos)
	n_all_sb = float(len(sb))
	frac_inter = float(nsb/n_all_sb)	
	n_arg = len(arg); n_lys = len(lys); n_glu = len(glu); n_asp = len(asp)
	n_charged_res = float(len(arg) + len(lys) + len(glu) + len(asp))
	perc_arg = float(n_arg/n_charged_res); perc_lys = float(n_lys/n_charged_res);perc_glu = float(n_glu/n_charged_res);perc_asp = float(n_asp/n_charged_res)
	res_fracs = (perc_arg,perc_lys,perc_glu,perc_asp)
	return nsb, nres, n_branched_per_sb_res, qpqn, frac_inter, res_fracs



    


########################################## loop through data dictionary, analyze and compare results within each family
import texttable as tt
from pyrosetta import *
init()
from pyrosetta.toolbox import get_secstruct
from pyrosetta.rosetta.core.scoring.sasa import *
ofile = open('inter07.txt', 'w')
avg_all_therm = []; avg_all_meso = []					#lists to hold averaged values for each parameter from each protein family
avg_thermo_nbranched = []; avg_meso_nbranched = []
avg_thermo_res_fracs = []; avg_meso_res_fracs = []
avg_thermo_qpqn = []; avg_meso_qpqn = []
avg_therm_fracs = []
avg_meso_fracs = []
the_keys = []
greater_nsb = []
greater_branching = []
higher_lys = []
higher_glu = []
less_asp = []
higher_arg = []
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
	thermo_res_fracs = []; meso_res_fracs = []
	thermo_qpqn = []; meso_qpqn = []
	therm_frac = []; meso_frac = []	
	for ptn in thermos:
		my_nsb, my_nres, n_branched_res, qpqn, frac_inter, res_fracs  = return_SB(ptn, 0.0, 7.0) 
		nsb_per_res = float(my_nsb/my_nres)	
		thermo_nsb.append(nsb_per_res)	
		thermfracnsb.append(my_nsb)
		thermfracnres.append(my_nres)
		thermo_n_branched.append(n_branched_res)
		thermo_qpqn.append(qpqn)
		thermo_res_fracs.append(res_fracs)
		therm_frac.append(frac_inter)
	for ptn in mesos:
		my_nsb, my_nres, n_branched_res, qpqn, frac_inter, res_fracs = return_SB(ptn, 0.0, 7.0) 
		nsb_per_res = float(my_nsb/my_nres)	
		meso_nsb.append(nsb_per_res)	
		mesfracnsb.append(my_nsb)
		mesfracnres.append(my_nres)
		meso_n_branched.append(n_branched_res)
		meso_res_fracs.append(res_fracs)
		meso_qpqn.append(qpqn)
		meso_frac.append(frac_inter)
	mean_therm_frac = take_mean(therm_frac)
	mean_meso_frac = take_mean(meso_frac)	
	avg_therm_fracs.append(mean_therm_frac)
	avg_meso_fracs.append(mean_meso_frac)	
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
	therm_avg_qpqn = take_mean(thermo_qpqn); meso_avg_qpqn = take_mean(meso_qpqn)
	avg_thermo_qpqn.append(therm_avg_qpqn); avg_meso_qpqn.append(meso_avg_qpqn)
	if therm_avg_qpqn > meso_avg_qpqn:
		higher_qpqn.append(therm_avg_qpqn)	
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
	
		


				
	
	
#################################   write overall avgs to outfile with statistical analysis
import scipy
from scipy import stats

n_families = len(the_keys)
n_greater_nsb = len(greater_nsb)
n_greater_branching = len(greater_branching)
n_higher_lys = len(higher_lys)
n_higher_glu = len(higher_glu)
n_higher_arg = len(higher_arg)
n_lower_asp = len(less_asp)
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
therm_nsb_array = scipy.array(avg_therm_fracs)    #frac inter
meso_nsb_array = scipy.array(avg_meso_fracs)
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
overall_nsb = "\nTHE AVG frac sb inter subunit FOR THERMOPHILES IS: " + str(therm_nsb_mean) + " WITH STANDARD DEVIATION: " + str(therm_nsb_std) + ", VARIANCE: " +  str(therm_nsb_var) + " AND STANDARD ERROR: " + str(therm_nsb_sem) + "\nTHE AVG FOR MESOPHILES IS: " + str(meso_nsb_mean) + " WITH STANDARD DEVIATION: " + str(meso_nsb_std) + ", VARIANCE: " + str(meso_nsb_var) + " AND STANDARD ERROR : " + str(meso_nsb_sem) + "\nTHE T STATISTIC IS: " + str(nsb_tstat) + " AND THE P VALUE IS: " + str(nsb_pvalue)
ofile.write(overall_nsb)

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

ofile.write('\n')
nsbdata = "\nDATA FOR NSB/NRES: " + "\nTHERMOPHILES = " + str(avg_all_therm) + "\nMESOPHILES = " + str(avg_all_meso)
ofile.write(nsbdata)


ofile.write('\n')
nbrdata = "\nDATA FOR N BRANCHED: " + "\nTHERMOPHILES = " + str(avg_thermo_nbranched) + "\nMESOPHILES = " + str(avg_meso_nbranched)
ofile.write(nbrdata)



ofile.write('\n')
resdata = "\nDATA FOR RES PREFERENCES IN SB: " + "\nTHERMOPHILES = " + str(avg_thermo_res_fracs) + "\nMESOPHILES = " + str(avg_meso_res_fracs)
ofile.write(resdata)


ofile.write('\n')
qpqndata = "\nDATA FOR qpqn: " + "\nTHERMOPHILES = " + str(avg_thermo_qpqn) + "\nMESOPHILES = " + str(avg_meso_qpqn)
ofile.write(qpqndata)


ofile.close()	