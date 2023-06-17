import numpy as np

# zero:  make a array fill with zero
arr_zero=np.zeros(4)
# making a two dimentional array of 3, 4
# make a 2-D array fill with zero
arr_zero1=np.zeros((3,4))
print(arr_zero)
print(arr_zero1)


# fill 1d array with 4 element
arr_one=np.ones(3)
print(arr_one)

arr_one2=np.ones((4,4))
print(arr_one2)




# empty array:: create a empty array fill with previous data
arr_em = np.empty(4)
print(arr_em)



# range::
# this create a range between 1 to 3 :: having four elemnt 
arr_rn=np.arange(4)
print(arr_rn)





# digonal element fill with 1 ::
# eg: 1 0 0
    # 0 1 0
    # 0 0 1


arr_dia=np.eye(3)
print(arr_dia)

arr_di=np.eye(5,5)
print(arr_di) 




# linsspace::  Create  an array with values that arr spaced linerly in a spevified interval 
arr_lin = np.linspace(0,20,num=5)
print(arr_lin)