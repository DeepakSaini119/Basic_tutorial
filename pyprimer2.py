#Classes, functions and imports
class vect:
	def __init__(self,idx,idy):
		self.idx = idx
		self.idy = idy
		self.print_vect()

	def print_vect(self):
		print "X coord:",self.idx
		print "Y coord:",self.idy

vec1 = vect(1,2)
vec2 = vect(3,4)


#Importing functions from other python files.
from arguments import get_options
opts = get_options()
print "Infile specified : ",opts.in_file

#Pandas
import pandas as pd
from pandas import DataFrame as df

cur_df = df.from_csv('test2.csv, idy, idy')
cur2_df = df.from_csv('test3.csv')
cur3_df = cur_df.join(cur2_df,lsuffix='_initial')

#ipdb
import ipdb
#Uncomment to set a checkpoint
#running with a checkpoint set automatically opens up ipdb. Can use commands like step, continue and locals() for debugging.
#ipdb.set_trace()

#plotting
from matplotlib import pyplot as plt
ax = [1,2,3,4,5]
ay = [3,4,2,5,1]
az = [1,2,3,4,5]

plt.scatter(ax, ay)
plt.plot(ax,az,'r')
plt.show()
