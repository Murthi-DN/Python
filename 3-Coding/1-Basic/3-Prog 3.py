#Python Program for factorial of a number

num=int(input("Enter a number"))

fact=1

while (num>1):
    fact*=num
    num-=1

print("Factorial of ", num, " is", fact)
