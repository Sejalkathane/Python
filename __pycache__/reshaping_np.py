import numpy as np
var=np.array([[13,43],[23,5]])
print(var)
print()
# give shape eg: (2,2)
print(var.shape)


a=np.array([1,2,3,4],ndmin=4)
print(a)
print(a.shape)



# conversion of dimention in array

# 1D to 2D
b=np.array([1,2,3,4])
# reshape  convert 1 to 2d as we provide dimention
c=b.reshape(2,2)
# d=b.reshape(2,4)
print(c)
# print(d)


var2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
ans=np.reshape(2,3,2)
print(ans)