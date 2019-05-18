'''
dataset = {
'1tyoA,2e0cA':'6c0e-A',
}
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
	dists = []
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
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		for x in asp:
			a2 = pose.residue(x).xyz("OD1") #likewise both asp oxygens
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
	for i in arg:
		a1 = pose.residue(i).xyz("NH1")  
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		a1 = pose.residue(i).xyz("NH2")  #counting both arg nitrogens as charged 
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		a1 = pose.residue(i).xyz("NE")  #3RD ARG NITROGEN
		for x in glu:
			a2 = pose.residue(x).xyz("OE1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OE2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
		for x in asp:
			a2 = pose.residue(x).xyz("OD1")
			vector = a1 - a2
			a3 = pose.residue(x).xyz("OD2")
			vector2 = a1 - a3
			if dcutlow < vector.norm() <= dcuthi or dcutlow < vector2.norm() <= dcuthi:
				if (i,x) not in pairs:
					if vector.norm()<vector2.norm():
						ip_dist = vector.norm()
						pairs.append((i,x))
						dists.append(ip_dist)
					else:
						ip_dist = vector2.norm()
						pairs.append((i,x))
						dists.append(ip_dist)																													
	davg = take_mean(dists)		
	return davg
	
	

 			
from pyrosetta import *
init()
ofile = open('Davg07.txt', 'w')
avg_all_therm = []; avg_all_meso = []	
the_keys = []
lower_avg = []				
for key in dataset.keys():
	the_keys.append(key)
	thermos = return_thermos(key)
	mesos = return_mesos(key)
	thermodavg = []; mesodavg = []
	for ptn in thermos:
		davg = return_SB(ptn, 0.0, 7.0) 
		thermodavg.append(davg)
	for ptn in mesos:
		davg = return_SB(ptn, 0.0, 7.0) 
		mesodavg.append(davg)		
	avg_therm_davg = take_mean(thermodavg); avg_meso_davg = take_mean(mesodavg)		
	avg_all_therm.append(avg_therm_davg)										
	avg_all_meso.append(avg_meso_davg)
	if avg_therm_davg < avg_meso_davg:
		lower_avg.append(avg_therm_davg)
	
n_families = len(the_keys)
n_loweravg = len(lower_avg)	
	
import scipy
from scipy import stats	
	
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
overall_nsb = "\nTHE davg FOR THERMOPHILES IS: " + str(therm_nsb_mean) + " WITH STANDARD DEVIATION: " + str(therm_nsb_std) + ", VARIANCE: " +  str(therm_nsb_var) + " AND STANDARD ERROR: " + str(therm_nsb_sem) + "\nTHE davg FOR MESOPHILES IS: " + str(meso_nsb_mean) + " WITH STANDARD DEVIATION: " + str(meso_nsb_std) + ", VARIANCE: " + str(meso_nsb_var) + " AND STANDARD ERROR : " + str(meso_nsb_sem) + "\nTHE T STATISTIC IS: " + str(nsb_tstat) + " AND THE P VALUE IS: " + str(nsb_pvalue)
ofile.write(overall_nsb)
n_fam_observed = "\nTHE davg INCREASED IN " + str(n_loweravg) + " OUT OF " + str(n_families) + " PROTEIN FAMILIES."
ofile.write(n_fam_observed)

ofile.close()	