# the only diff between list and array and list is :
# array having dimilar data type element

from array import *
# * means all
# see type code in python once

# "i" for integer
val=array('i',[1,2,4,2,5])
val.reverse()
print(val)
print(val[2])

# for i in range(len(val)):
    #   print(val[i])


for i in val:
    print(i)

