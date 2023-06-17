import numpy as np
# random function:: 
# 1.rand() : generate a random num. between 0 to 1
# 2.randn() : generate value close to zero : may be negative or positive
# 3.ranf(): include 0 generate between 0 to 1





# 1.rnad()
 
# //generate a random array between 0 to 1
var=np.random.rand(8)
print(var)
# generate a random array with 3 * 3 matrix
pr=np.random.rand(3,3)
print(pr)




# 2. rnadn():number may be negative or positive
a1=np.random.randn(4)
print(a1)

a2=np.random.randn(3,3)
print(a2)




# 3. close to zero less than 1 0 include but 1 not
b1=np.random.ranf(4)
print(b1)

# b2=np.random.ranf(3,3)
# print(b2)




# 4.randint(): generate between given range
#  randint(min, max, no you want to generate)
c1=np.random.randint(50,100,10)
print(c1)