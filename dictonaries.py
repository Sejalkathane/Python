# having a key value pair

# dic not having a similar key value;

mydict={"1":"sejal",
        "2":"Prasanna",
        "3":["Gita","sk","pk"],
        "4":"Nita"}
print(mydict)

# also use get to acess item
print(mydict.get("3"))

# keys :  give all key of dict
print(mydict.keys())

# values: this give value of all item in dict
print(mydict.values())

# return its key value
print(mydict["3"])

# find length of dict
print(len(mydict))



# ????????????????????????????????

# best example of dict
# we have key inside a key
d={'k1':"sejal" , 'k2':[0,1,2] , 'k3':{'insidekey':100}};

print(d['k2'])
print(d['k3'])
#  acess inside key
print(d['k3']['insidekey'])



# operation on dict
print(d['k1'].upper())

# change k1
d["k1"]="gitanjali"
print(d)