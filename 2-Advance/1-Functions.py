def newFun(Name):
    print("Hi, ", Name)

newFun("Murthi")



#Return

def add(a,b):
    return (a+b)

r=add(1,2)
print(r)



#Return multiple

def multi():
    return 1,2,3

a=multi()
print(a)



#Local and Global vars

b=10

def show():
    b=20
    print(b)

print(b)
show()


#Accessing Global val inside fun with same name

a=10

def show():
    a=20
    print(a)
    print(globals()['a'])

show()