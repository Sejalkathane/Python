from functools import reduce
# map::
# theory just like a cpp

# def is_even(n):
#    return n%2==0


# filter the element depend on provided condition :

# filter(functin,iterable)


# nums=[2,1,4,2,6,4,7,8]
# evens=list(filter(lambda n:n%2==0,nums))


# print(evens)
# # print(double)




# def f(x):
#     if(x%3==0):
#          return x

# a=[1,2,3,4,5,6,7,8,9]
# fil=list(filter(f,a));
# print(fil)






# # map:: 
# # map(funtion,ierable)
# # map is use to apply single trnaforamable fucntion to all element in function then we use map
# def cube(x):
#      return x*x*x
# n=[1,23,4,56,7]

# new=list(map(cube,n))
# print(new)


# l=[13,43,5,671,2,75,14]
# new=list(map(lambda x:x+2,l))
# print(new)





# reduce::
# it reduce all alue in a single mean value for example sum

r=[76,475,90,33,7]

sum=reduce(lambda a,b:a+b , r)
print(sum)


def prod(x,y):
    return x*y

mul= reduce(prod,r)
print(mul)
