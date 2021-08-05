
string = str(num)
string = list(string)
string.reverse()
string = ''.join(string) #list to str
num = int(string)

print(num)





or





while(number != 0)   
	remainder = number % 10  
	reverse = reverse * 10 + remainder 
	number = number/10

print(reverse)