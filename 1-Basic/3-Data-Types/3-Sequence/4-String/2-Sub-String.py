str = 'Hello World!'

print(str) # Prints complete string
print(str[0]) # Prints first character of the string
print(str[2:5]) # Prints characters starting from 3rd to 5th
print(str[2:]) # Prints string starting from 3rd character
print(str[:3]) # Prints string till 3rd character

print(len(str))

#Slicing
print(str[-3:-1])
print(str[1:-1:2])

#To come from reverse order
print(str[::-1])

var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#String Update
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
