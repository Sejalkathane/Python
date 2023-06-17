import numpy as np

# Join:: you can join only when your no of data element is same

# 1D
var1=np.array([1,2,3,4])
var2=np.array([5,40,31,23])

c=np.concatenate([var1,var2])
c.sort()
print(c)


# 2D::
ar1=np.array([[2,641,7,3],[52,65,27,8]])
ar2=np.array([[8,1,6,2],[53,7,3,7]])

# axis can provide we can merge as row=1 or col=0
d=np.concatenate([ar1,ar2],axis=1)
print(d)






# SPLIT :: 
v1=np.array([1,2,3,4])
print(v1)
new=np.array_split(v1,3)
print(new)


# 2D:
ar1=np.array([[2,641,7,3],[52,65,27,8]])
n1=np.array_split(ar1,2,axis=1)
print(n1)



#3D 
ar3=np.array([[[1,2,3,4],[9,8,65,3],[3,5,24,62]]])
n3=np.array_split(ar3,2,axis=0)
print(n3)



