import numpy as np

var=np.array([21,8,27,9,6,54,90,38,3,54,23,82])
print(var)


# insert having three parameter::   {{ array name , position ,value}}

v=np.insert(var,3,500)
print(v)
# we can pass lisr also in position place::
v2=np.insert(var,[2,3,7],2222)
print(v2)
# you can laso use append 


var2=np.array([[1,34,5,2],[8,50,95,24]])
# x3=np.insert(var2,2,6,axis=1)
# x3=np.insert(var2,2,[9,6],axis=1)
x3=np.insert(var2,2,[9,6,5,2],axis=0)
print(x3)
