from random import shuffle
from random import randint
word="abcdef"

# print tuple in pair
# enumerate: return index and letter
for item in enumerate(word):
    print(item)



# zip function:: use to 
myl=[1,2,3]
myl2=['a','b','c']
myl3=[100,200,300]

for it in zip(myl,myl2,myl3):
    print(it)


# in

# return true or false
x='a' in 'a world'
print(x)



# shuffle a given list
myl=[1,2,3,4,5,6,7,8,9]
shuffle(myl)
print(myl)



# return random
print(randint(0,100))