import numpy as np
# create matrix in numpy:: 

var=np.matrix([[1,2],[5,6]])
print(var)
print(type(var))

var2=np.matrix([[1,2],[5,6]])
print(var*var2)    #matrix multiplication is diffrence 
print(var.dot(var2))   #give same as *


var1=np.array([[1,2,3,4],[5,6,7,8]])
var3=np.array([[1,2,3,4],[5,6,7,8]])
print(var1)
print(type(var1))
print(var1*2)
print(var1*var3)




#matrix function:: 
# 1. Transpose:: 
print()
print()
mat=np.matrix([[1,2,3],[8,3,6],[2,3,4]])
print(mat)
print()
# give transpose::
print(np.transpose(mat))
print()
print(mat.T)








# Swapaxes:: convert col to row and row to col
print(np.swapaxes(mat,0,1))



# INverse matrix:: 
m=np.matrix([[1,2],[4,5]])
print(np.linalg.inv(m))


# power of matrix::
print()
print(np.linalg.matrix_power(m,2))



# Determinent:: 
print()
print(np.linalg.det(m))

