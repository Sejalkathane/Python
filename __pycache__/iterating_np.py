import numpy as np

a=np.array([29,6,2,7,37,22])
print(a)
print()
# iterate data
for i in a:
    print(i)



# 2D
b=np.array([[1,23,4,51],[6,36,726,62]])
print(b)
# same as cpp
for i in b:
    for j in i:
       print(j)



#3D:
c=np.array([[[1,2,5,22],[63,8,2,46],[82,34,7,18]]])
print(c)

for i in c:
    for j in i:
        for k in j:
            print(k)



#   By USING FUNCTION IT MAKE EASY TO ITER :: nditer()

d=np.array([[[1,2,5,22],[63,8,2,46],[82,34,7,18]]])

# reduce for loop
for i in np.nditer(d):
    print(i)