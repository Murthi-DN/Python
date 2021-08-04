
from array import *
val=array('i', [1,2,3,4,5])

#Methods are same as List
print(len(val))

#How many times obj occured
print(val.count(5))

#To remove an element by index
print(val.pop(4))
print(val)

#To remeove specific obj
val.remove(4)
print(val)

#To add new array
val2=array('i', [4,5,6,7,8])
val.extend(val2)
print(val)

#To print obj's index
print(val.index(8))

#To add new elem at end
val.append(9)
print(val)

#To reverse whole array
val.reverse()
print(val)

#To insert at specific index
val.insert(0, 10)
print(val)
