s=set()
print(type(s))

#adding values to an empty set
s.add(4)
s.add(4) # adding a value repeatedly does not changes a set


s.add(5)
s.add((4,5,6,7,4,8,5))

#remove of an item
s.remove(5) # remove from the set 
print (len(s))
print(s)


print(s.pop()) # remove random element from the set

print(s)

s.clear() # it is used for clear the set

print(s)
