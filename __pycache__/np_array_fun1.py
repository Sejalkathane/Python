import numpy as np


# SEARCHING :: 
#   =>use where keyword

var1=np.array([13,2,68,24,971,2,67,257])
# return index and datatype  : give list and all position
x=np.where(var1==2)
print(x)
x2=np.where((var1%2)==0 )
print(x2)





# SEARCH SHORT ARRAY:: It give the position where we need to insert given element so sorted array should be maintned

var2=np.array([1,2,3,5,6,7,8])
# x3=np.searchsorted(var2,4)
x3=np.searchsorted(var2,[2,3,6])   # we can also pass list 

print(x3) 





#SORT ARRAY:: 
var3=np.array([2,5,16,7,268,23,793,87,2,872,3])
print(np.sort(var3))

st=np.array(["sejal","pk","nk","ak","gk"])
print(np.sort(st))

# sort 2D array::
var4=np.array([[4,15,1,6],[6,28,24,65]])
print(np.sort(var4))

