import numpy as np



# SHUFFLE FUNCTION:: 
var=np.array([21,8,27,9,57,567,90,38,3,54,23,82])
np.random.shuffle(var)
print(var)



#UNIQUE:: give unique value

x=np.unique(var,return_index=True,return_counts=True)
print(x)



#Resize():: 
print(np.resize(var,(3,3)))




