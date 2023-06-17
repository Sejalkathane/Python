import pandas as pd 

# dropna:: 


var=pd.read_csv('s.csv')
# print(var)
# print(var.dropna())



#''''''' If i want to drop by column then i can:: 
# print(var.dropna(axis=1))


#''''''''''' Remove subset value from dataset::
# print(var.dropna(subset=["Duration"]))


# '''''''''remove null value and print new dataset
# print(var.dropna(inplace=True))


# '''''''remove those which having single null value::
# print(var.dropna(thresh=2))




# ################ FILLNA::::: INSTED OF NULL FILL ANY VALUE:
# print(var.fillna("python"))

# in duration col we put python insted of null and in pulse it c
print(var.fillna({"Duration":"py" , "pulse":"c"}))

