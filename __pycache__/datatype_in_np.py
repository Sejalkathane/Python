import numpy as np

# Data type:: 
# 1. bool_
# 2. int_
# 3. unit8
# 4. float_ ........... many more


var=np.array([1.2,"s",3,4])
print("data type ",var.dtype)   #give integer 32 bit data

a=np.array(["a","v","d"])
print("data type ",a.dtype) 



# convertion of datatype:
# give short form of datatype:
# eg : i-interger , b-boolean  , f-float etc..

x=np.array([1,2,3,4],dtype="S")
# this use as a function
new=np.float32(x)
print(x.dtype)
print(x)
print(new.dtype)
print(new)




# you can convert directly also:: by using{ """" astype """"}
b=np.array([1,2,3,4])
new=b.astype(float)
print(b.dtype)
print(b)