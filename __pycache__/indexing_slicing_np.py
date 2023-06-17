import numpy as np
# indexing and slicing::

# Indexig::
var=np.array([9,11,34,1])
#             0, 1 ,2, 3


print(var[1])
print(var[-1])   #start from back



var2=np.array([[1,23,4,32],[45,6,1,7]])
print(var2)
print(var2.ndim)

# get 0,2 element:
print(var2[0,2])


var3=np.array([[[1,23,4],[56,2,5],[2,6,7]]])
print(var3)
print(var3.ndim)
print()
print(var3[0,2,2])




# Slicing::
# eg:[1,2,3,4,5]:: need data from 2 to 4
# slicing==>  [start:stop:step]

#  1D slicing
x=np.array([1,2,3,4,5,6,2,4,65,23,45,5,78,783,1,12])
print(x)
print()
print(x[2:10:2])

# start to end-
print(x[3:])




#2D
v=np.array([[2,3,4],[12,34,2],[42,3,4]])
print(v)
print()
# provide: row no : then slicing
print(v[1,1:])
