# Arithmetic Operation in NumPy Array

# 1. a+b: np.add(a,b)
# 2. a-b: np.subtract(a,b)
# 3. a*b: np.multiply(a,b)
# 4. a/b: np.divide(a,b)
# 5. a%b: np.mod(a,b)
# 6. a**b: np.power(a,b)
# 7. 1/a: np.reciprocal(a)



import numpy as np
var=np.array([1,2,3,4])
var_add = var+3
print(var_add)


a=np.array([1,2,3,4])
b=np.array([9,8,7,6])
# add a and b
c=a+b
print(c)

d=a-b
print(d)

e=a*b
print(e)

f=a%b
print(f)

g=a/b
print(g)

h=1/a
print(h)




# function:: 
# eg:
x=np.multiply(a,b)
print(x)




# 2D array::
two_arr=np.array([[1,2,3,4],[4,3,2,1]])
ccc=two_arr*3
print(ccc)



# 3D array::
three_arr1=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
three_arr2=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
q=three_arr1+three_arr2
print(q)