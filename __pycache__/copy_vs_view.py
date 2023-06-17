import numpy as np
var=np.array([1,2,3,4])

# copy the given array:
co=var.copy()
print(co)
var[2]=40

# view :
v=var.view()
print(v)


# difference betn copy vs view
# """  copy owns the data   ||  view does not own the data
# """  copy is new array    ||  view original array
# """  in copy data changes does not reflect  || in view changes are reflected
# ???????   copy data not change if we change original but view does