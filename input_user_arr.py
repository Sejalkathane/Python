from array import *

# inisilize array
arr=array('i',[])

n=int(input("Enter the length of array: "))

for i in range(n):
    x=int(input("Enter the value: "))
    arr.append(x)


print(arr)
for i in range(n):
    print(arr[i])


# seach in array

num=int(input("enter which element you want to search: "))

# k is for index
k=0
for i in arr:
    if(num==i):
        print(k) 
        break
    
    k+=1





