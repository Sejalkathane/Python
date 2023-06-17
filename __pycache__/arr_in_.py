import numpy as np
a=np.array([1,2,3,4])
print(a)
print(type(a))
print(a.ndim)


# //take input in array
# l=[]  
# x=int(input("Please enter how many array size you need: "))
# for i in range(x):
#     a=int(input("please enter elm : "))
#     l.append(a)


# //  convert in form of array
# print(np.array(l))




# types of array::
# 1. 1D Array   [1,2,3,4]
# 2. 2D Array   [[1,2,3,4]]
# 3. 3D Array    [[[1,2,3,4]]]
# 4. Higher Dimentional Arrays

# ndim to find dimensition



# //   we need same 2* 2  
ar2=np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print(ar2.ndim)


# 4 dimentional array
ar3=np.array([[[[1,2,3],[9,8,7],[6,5,4],[12,32,45]]]])
print(ar3)
print(ar3.ndim)





#  n dimentional array::
# 10 dimention array:
ar4=np.array([1,2,3,4],ndmin=10)
print(ar4)

