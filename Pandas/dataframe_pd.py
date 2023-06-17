# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd

x=[1,23,4,8,657,37,9]
var=pd.DataFrame(x)
print(var)



# length must be sameb 
data={"mark":[12,35,12,64],
      "sub":["math","sci","eng","sst"],
      "rollno":[1,2,3,4]}

# da=pd.DataFrame(data)
# we can give specific column also
da=pd.DataFrame(data,columns=["mark"])

# change index no:
id=pd.DataFrame(data,index=["a1","a2","a3","a4"])
print(id)

# get a particular data
print()
print(data["mark"][2])




# making a row in dataframe
list_1= [[1,2,3,4,5],[43,46,13,77]]
var2=pd.DataFrame(list_1)

print(var2)





# Creating dataframe using series:
sr={"s1":pd.Series([12,3,4,5]),"s2":pd.Series([46,32,94,57])}

serda=pd.DataFrame(sr)
print(serda)