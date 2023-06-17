# 1. Series
# 2.DataFrame
# 3.Panel



# 1.Series::
#    It is as a one-dimensional array that is capable of storing various data type

import pandas as pd
x=[16,142,53,84,58]
# ??  printing index with value::
a=pd.Series(x)
# print(type(a))
# print(a)
# print(a[2])
   


dic={"name":['python','c','c++','java'],"por":[12,13,14,15,],"rank":[1,4,3,2]}

var1=pd.Series(dic)
print(var1)

print(var1[0])


s=pd.Series(12,index=[1,2,3,4,5,6,7,8,9])
print(s)
print(type(s))


# why we use pandas insted of numpy

# because if we want to add two array or list which having not same number then numpy not support this but pandas can

# in numy it show broadcast error
s1=pd.Series(12,index=[1,2,3,4,5,6,7])
s2=pd.Series(12,index=[1,2,3])
print(s1+s2)

print()



# change index name
x1=[112,56,872,27]
cal=pd.Series(x1,index=["day1","day2","day3","day4"])
print(cal)



