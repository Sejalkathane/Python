# CSV VS EXCEL

# CSV : #1.output in plain text
        # 2. Comma Sepreated Values

#EXCEL: # 1.Data in binary format
        # 2.Data store in worksheet




# WRITE CSV file

import pandas as pd

# dis={"a":[1,23,4,6],"b":[8,45,9,3],"c":[45,27,12,8]}

# d=pd.DataFrame(dis)
# print(d)

# # d.to_csv("Test_new.csv")
# # remove index::
# d.to_csv("Test1.csv",index=False)
# print(d)





# READ A CSV FILE:

#'''''''''' We Have csv file we need to read this :: 

# r=pd.read_csv('weather.csv')
# # print(r.to_string()) # to_string use to print entire DataFrame



# READ SPECIFIC ROW OR COL 

#''''''''' print(perticular row) : give starting 2 row

r=pd.read_csv('weather.csv',nrows=2)
# print(r)


#'''''''' get specific column:

r=pd.read_csv('weather.csv',usecols=["MaxTemp","Rainfall"])

r=pd.read_csv('weather.csv',usecols=[0,4])  #''''''''''give 0th and 4th to -- column
# print(r)


# SKIP ROW::
r1=pd.read_csv("weather.csv",skiprows=[0,3])
# print(r1)




# Make column as a index::
red=pd.read_csv('weather.csv',index_col="Rainfall")
# print(red)



# HEADER:: 2nd col become header
h=pd.read_csv('weather.csv',header=2)
# print(h)




#NAME:: CHANGE:
ch=pd.read_csv('weather.csv',names=["R1","R2","R3","R4"])
# print(ch)




