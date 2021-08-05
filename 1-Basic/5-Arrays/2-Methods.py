
from array import *

val=array('i', [1,2,3,4,5])

val.insert(0, 10)
val.remove(4)

val.append(9)
print(val.pop(4))

val2=array('i', [4,5,6,7,8])
val.extend(val2)

print(len(val))

val.reverse()

print(val.count(5))

print(val.index(8))
