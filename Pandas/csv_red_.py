import pandas as pd
import numpy as np

r1=pd.read_csv('weather.csv')
# print(r1)


#'''''''''''''' give starting value, end value ,and step they move

# USE INDEX{{{{}}}}
# print(r1.index)




#'''''''''''''' GET COLUMN NAME:: 

# USE COLUMNS{{{{}}}}
# print(r1.columns)



# '''''''''''''ALL DATA EX: MIN MAX, COUNT,MEAN ETC:: PRINT
# print()

# USE DESCRIBE{{{{{}}}}}
# print(r1.describe())




#"""""""""" HEAD : GIVE STARTING DATA """""""
# print(r1.head(5))



# """"""""" TAIL : GIVE LAST DATA """"""""" 
# print(r1.tail())



# """"""""" GIVE SPECIFIC RANGE DATA """"'""
# print(r1[5:10])
# print(type(r1))



# '''''''' PRINT INDEX IN ARRAY '''''''''''
# print(r1.index.array)


# '''' ALL DATA BECOME NUMPY ARRAY '''': in thios we get all data
# print(r1.to_numpy())
# v=np.asarray(r1)
# print(v)



# ''''' GIVE INFO ABOUT DATA '''''
# print(r1.info())



#''''''' PUT DATA IN DECENDING ORDER :: ''''''''
# print(r1.sort_index(axis=0,ascending=False))




# :::::: Locate Row :::::
# changes in 0th row in rainfall column
# r1.loc[0,"Rainfall"]="Sejal"
# print(r1)



# give 2nd and 3rd row data from col
# print(r1.loc[[2,3],["MinTemp","Rainfall"]])



# ......... iloc give perticular data::............
print(r1.iloc[0,1])



 

