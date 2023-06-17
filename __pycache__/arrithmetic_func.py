# Arithmetic Function:: 
# 1.np.min(x)
# 2.np.max(x)
# 3.np.argmin(x)  : positon of minimum element
   # np.argmax(x)  : positon of maximum element
# 4.np.sqrt(x)
# 5.np.sin(x)
# 6.np.cos(x)
# 7.np.cumsum(x)




import numpy as np

var=np.array([13,12,343,4])
print("min no is: ",np.min(var))
print("max no is: ",np.max(var))
print("position of min no is: ",np.argmin(var))
print("position of max no is: ",np.argmax(var))


two_d=np.array([[64,67,23,81],[13,65,34,93]])
# we can also traverse through axis :: for col =0 and row=1
print(np.min(two_d,axis=1))  #give output between every row
print(np.min(two_d,axis=0)) # give output between every col 

print(np.argmin(two_d,axis=1))  #give index of min element

# print(np.min(two_d))
# print(np.max(two_d))
# print(np.argmin(two_d))


# squre root
print(np.sqrt(var))


# sin ans cos:
var2=np.array([1,2,3])
print(np.sin(var2))
print(np.cos(var2))


# cumsum:: given add of one by one no store in next position 
# eg: [1,2,3]=>[1,3,6]

print(np.cumsum(var2))

