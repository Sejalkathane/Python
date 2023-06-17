import pandas as pd

var=pd.DataFrame({"A":[1,23,4],"B":[9,94,42]})
print(var)

print()
# ?Add two column and print in c
var["C"]=var["A"]+var["B"]
var["D"]=var["A"]-var["B"]
var["E"]=var["A"]*var["B"]

var["F"]=var["A"]/var["B"]

print(var)


# logical :
# return true false
var["X"]=var["A"]<=3
print(var)


# var.insert("index_no,position_name",value you want to insert)
# make a duplicate copy of A

# var.insert(1,"U",var["A"])
var.insert(1,"U",[23,75,32])

print()
print(var)




# Delete:: 
# delete B
var.pop("B")
print(var)

# Delete A
del var["A"]
print(var)