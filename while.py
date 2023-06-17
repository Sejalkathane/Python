x=0

while x<5:
    print(x)
    x+=1
else:
    print("x=5")


x=[1,2,3]
  
# pass just pass do nothing
for item in x:
    pass
print("end")



# dont print condition just pass
str="Sejal"
for l in str:
    if l=='e':
        continue
    print(l)


# break the
for l in str:
    if(l=='j'):
        break
    print(l)