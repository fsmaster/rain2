import numpy as np
import pandas as pd


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
iterations=2
chunk=1000000

bitgen = np.random.PCG64(seed=0)
rng = np.random.Generator(bitgen)

my_array=rng.integers(low=1, high=70, size=chunk*iterations)
print(my_array)
df = pd.DataFrame(my_array, columns=["number"])
print(df.T.shape)
df.T.to_csv(str("sample-")+'.csv',index=False,header=False,line_terminator=',')


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

print("-------------------------")


for i in range(0,iterations):
# repeat, advance the bitgen by 1
	bitgen = np.random.PCG64(seed=0).advance(round(chunk*i/2))
	rng = np.random.Generator(bitgen)

	my_array=rng.integers(low=1, high=70, size=chunk)
	print(my_array)
	df = pd.DataFrame(my_array, columns=["number"])
	print(df.T.shape)
	df.T.to_csv(str(0)+'.csv',index=False,header=False,mode='a',line_terminator=',')
