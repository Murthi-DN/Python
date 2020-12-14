#A tuple is a collection which is ordered and unchangeable
#Immutable

tup=(1,2,3,4,5)
print(tup)

#Get value by index
print(tup[1])

#Tuple is faster than list
#Bcz, since we don't change values, it's faster

#To find specific obj's index
print(tup.index(2))

#To find an obj occurance
print(tup.count(5))

print(max(tup))
print(min(tup))
print(sum(tup))

#All are similar to list methods which are unchangeable methods