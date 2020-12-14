from array import *

val = array("i", [])
size = int(input("Enter Size"))

for i in range(size):
    value=int(input("Enter Number"))
    val.append(value)

print(val)