"""
String are used to store text data
"""

info="Murthi from India"
print(info)

"""
Text stores in sequence, with memory address, we can access by index 0 to n-1 
"""

print(info[0])

"""
Strings are immutable, we can't change
Ex:
"""

#Error
#info[0]="A"
print(info)

name="Murthi's Naganna"
name='Murthi"s Naganna'

name="Murthi's Naganna's Murthi"
name='Murthi "Naganna"'

#Multi line
name="""Murthi
Naganna"""

print(name)

#Internally it adds \n


#String concat by +
n1="Murthi"
n2="Naganna"
print(n1+n2)
print(n1+" ", n2)


#Add int with str
name="Murthi"
age=24
print(name+str(age))


str = 'Hello World!'
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string
