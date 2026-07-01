# print(1,23,43)

# //lets amke a list to store more number of value in array like structure

nums=[1,3,4,5,43]
# extract data
print(nums[0])
# want to print from till end we can write as

print(nums[0:])
print(nums[-2])

# list of string
names=['sk','pk','gk','nk']
print(names[0:])

values=[9.5,"sk",23]
print(values[0])


# list inside a list
mst=[nums,names]
print(mst)


# simple function
nums.sort()
print(nums)

# append insert at last
nums.append(21)
print(nums)

# in insert we need to give  index and then value
nums.insert(2,1534)
print(nums)


# remove
nums.remove(21)
print(nums)

# pop use to remove element from index place 
#  pop without index value give pop last one
nums.pop(1)
print(nums)


# del is use to delete a slicing range also
# delete all element after 2
del nums[2:]
print(nums)


# add multiple value
nums.extend([13,45,65,7])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))