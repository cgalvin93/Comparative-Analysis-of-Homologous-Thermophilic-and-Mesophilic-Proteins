import scipy
import numpy
import matplotlib.pyplot as plt
from scipy import stats

def array(thermlist,mesolist):
	thermarray = scipy.array(thermlist)
	mesarray = scipy.array(mesolist)
	return thermarray, mesarray
	
thermarray,mesarray = array(THERMOPHILES, MESOPHILES)

thermophiles = plt.hist(thermarray, 20, alpha=0.5, color='b', label='Thermophiles')
mesophiles = plt.hist(mesarray, 20, alpha=0.5, color='g', label='Mesophiles')
plt.legend(loc=1)
plt.ylabel('Frequencies')
plt.grid(True)
plt.xlabel('Normalized Number of Charged Residues')
plt.savefig('Nq.png')

plt.clf()

###########violin plots

from matplotlib.axes import Axes
meso5array = scipy.array(MESOPHILES5)
therm5array = scipy.array(THERMOPHILES5)
meso7array = scipy.array(MESOPHILES7)
therm7array = scipy.array(THERMOPHILES7)
datasett = [meso5array,therm5array,meso7array,therm7array]

ax = plt.gca()
violin_parts = Axes.violinplot(ax,datasett,vert=False,showmeans = True, showextrema = True)
plt.setp(ax, yticks=[y+1 for y in range(len(datasett))],
        yticklabels=['Meso 5.0', 'Therm 5.0', 'Meso 7.0', 'Therm 7.0'],
        )       
plt.setp(violin_parts['bodies'][0], facecolor='green', edgecolor='black')   
plt.setp(violin_parts['bodies'][1], facecolor='blue', edgecolor='black') 
plt.setp(violin_parts['bodies'][2], facecolor='green', edgecolor='black') 
plt.setp(violin_parts['bodies'][3], facecolor='blue', edgecolor='black') 
plt.xlabel('Ratio of Repulsive to Attractive Interactions')    
plt.savefig('R.png')
plt.show()
##########something else

pdbfetch 1be9
pdbstrip 1be9.pdb
pdbvol 1be9.pdb

def n_greater(list1,list2):
	greater = []
	for i in list1:
		index = list1.index(i)
		x = list2[index]
		if i > x:
			greater.append((i,x))
	result = len(greater)
	return result	
	
arg lys glu asp
	
arg = []
lys = []
glu = []
asp = []
def unpack(list):
	for (a,b,c,d) in list:
		arg.append(a)
		lys.append(b)
		glu.append(c)
		asp.append(d)
unpack(THERMOPHILES)
marg = []
mlys = []
mglu = []
masp = []
def munpack(list):
	for (a,b,c,d) in list:
		marg.append(a)
		mlys.append(b)
		mglu.append(c)
		masp.append(d)
munpack(MESOPHILES)		 
####################### bar graph
thermo_means = [5.32, 8.00, 5.10, 9.50]
meso_means = [4.75,6.00,5.80,6.90]
std_meso = [0.2,0.3,0.1,0.2]
std_therm = [0.2,0.2,0.2,0.2]
fig, ax = plt.subplots()
n_groups = 4
index = numpy.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = ax.bar(index, meso_means, bar_width,
                alpha=opacity, color='g',
                yerr=std_meso, error_kw=error_config,
                label='Mesophiles')
rects2 = ax.bar(index + bar_width, thermo_means, bar_width,
                alpha=opacity, color='b',
                yerr=std_therm, error_kw=error_config,
                label='Thermophiles')
ax.set_xlabel('Amino Acid')
ax.set_ylabel('Percent Composition')
ax.set_title('Charged Amino Acid Composition')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Arg', 'Lys', 'Asp', 'Glu'))
ax.legend()
fig.tight_layout()
plt.show()
plt.savefig('aa.png')