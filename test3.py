#iter calculation:
#10 -27mb
#100 - 270mb
#1000 - 2,7gb
#10000 - 27gb
#100000 - 270gb
#1000000 - 2,7tb

import numpy as np
import pandas as pd
import os
import logging,sys


logging.basicConfig(filename='test3.log', filemode='a', format='%(asctime)s [%(levelname)s] %(message)s ', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.info('test3 started')

#for i in range(0,5):
#rng = np.random.default_rng(0)
#print(rng)
#my_array=rng.integers(low=1, high=70, size=100)
#print(my_array)
#df = pd.DataFrame(my_array, columns=["number"])
#print(df.T.shape)
#df.T.to_csv(str(0)+'.csv',index=False,header=False)
#rng = np.random.default_rng(0).advance(1)
#

#rng = np.random.default_rng(1)
#print(rng)
#my_array=rng.integers(low=1, high=25, size=100000000)
#print(my_array)
#df = pd.DataFrame(my_array, columns=["number"])
#print(df.T.shape)
#df.T.to_csv('1.csv',index=False,header=False)



#file.write(str(a))
iterations=100000
chunk=1000000

#bitgen = np.random.PCG64(seed=0)
#rng = np.random.Generator(bitgen)

#my_array=rng.integers(low=1, high=70, size=chunk*iterations)
#print(my_array)
#df = pd.DataFrame(my_array, columns=["number"])
#print(df.T.shape)
#df.T.to_csv(str("sample-")+'.csv',index=False,header=False,line_terminator=',')


#iter 1
#bitgen = np.random.PCG64(seed=0)
#rng = np.random.Generator(bitgen)
#my_array=rng.integers(low=1, high=70, size=chunk)
#print(my_array)
#df = pd.DataFrame(my_array, columns=["number"])
#print(df.T.shape)
#df.T.to_csv(str(0)+'.csv',index=False,header=False,line_terminator=',')


#for i in range(6):
#    print(i, rng.random())

#print("-------------------------")
#try:
#	os.remove('0.csv')
#except:
#	pass

t0 = [5,15,38,47,65]
tm1 = [5,16,27,39,61]
print (t0[0])
t0_b1=t0[0]
t0_b2=t0[1]
t0_b3=t0[2]
t0_b4=t0[3]
t0_b5=t0[4]

candidates = pd.DataFrame(columns = ['tm1_b1', 'tm1_b2', 'tm1_b3', 'tm1_b4', 'tm1_b5', 't0_b1', 't0_b2', 't0_b3', 't0_b4', 't0_b5', 'tp1_b1', 'tp1_b2', 'tp1_b3', 'tp1_b4', 'tp1_b5'])
for i in range(0,iterations):
# repeat, advance the bitgen by 1
	print ("iter " +str(i))
	bitgen = np.random.PCG64(seed=0).advance(round(chunk*i/2))
	rng = np.random.Generator(bitgen)

	my_array=rng.integers(low=1, high=70, size=chunk)
	print(my_array)
	df = pd.DataFrame(my_array, columns=["number"])
	print(df)

#	print(df['number'][df['number']==5].index[0])
	ix=np.where(df['number']==t0_b1)
#	print(df.loc[145])
	print (ix[0])
	for i in ix[0]:
			if True:
#			try:
#				if( (df.loc[i+1][0]==t0_b2) & (df.loc[i+2][0]==t0_b3) & (df.loc[i+3][0]==t0_b4) & (df.loc[i+4][0]==t0_b5)  ):
				if( (df.loc[i+1][0]==t0_b2) & (df.loc[i+2][0]==t0_b3)  ):
					print ("found")
					tm1_b5=df.loc[i-1][0]
					tm1_b4=df.loc[i-2][0]
					tm1_b3=df.loc[i-3][0]
					tm1_b2=df.loc[i-4][0]
					tm1_b1=df.loc[i-5][0]

					tp1_b1=df.loc[i+5][0]
					tp1_b1=df.loc[i+6][0]
					tp1_b1=df.loc[i+6][0]
					print(df.loc[i][0])
					print(df.loc[i+1][0])
					print(df.loc[i+2][0])
					print(df.loc[i+3][0])
					candidates=candidates.append({'b1':1,'b2':2,'b3':3},ignore_index=True)
					logging.info(candidates)
#			except:
#				pass			
#	sys.exit()
#	df=df.T
#	a=df.to_numpy().flatten().tolist()
#	np.reshape(a.size, a)
#	ix=np.where ((50,60) in a)[0]
#	a=[1,2,3,40,50,6,7]
#	a=pd.DataFrame(a)
#	print(a.shape)
	
#	ix=np.searchsorted(a,[40,50])
#	print("ix")
#	print(ix)
#	print (a[ix])
#	print (a[ix+1])
#	if a[ix].shape[0]>0:
#		print("found")
#		print(a[ix].shape[])
#		print(a[ix])
#	print(df.T.shape)
#
#	term=","
#	if (i==iterations-1):
#		term="\n"
#	df.T.to_csv(str(0)+'.csv',index=False,header=False,mode='a',line_terminator=term)
