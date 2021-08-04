#Collection of Unique elements
#set = {}
#Doesn't follow sequence memory index
#So indexing is not supported

sets={1,2,3,4,5}
print(sets)

sets={1,2,3,4,5,5}
print(sets)

#Even if u add duplicate, gives only once

#No duplicates, No indexing

#To add an obj
sets.add(6)
print(sets)

#To remove an obj
sets.remove(6)
print(sets)

#To copy
s2=sets.copy()
print(s2)

#To clear
print(s2)
s2.clear()
print(s2)

print("-------")
sets.pop()
print(sets)

#Almost like list but no index related methods and no duplicates
