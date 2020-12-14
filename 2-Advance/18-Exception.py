#Else will be added when there is no exeption
#Finaly will be added whether exception or not, ex: Resource connection, File close...etc

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Division by 0")