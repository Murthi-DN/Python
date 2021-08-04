names=["IBM", "Microsoft", "Google"]

#To insert @ specific position
names.insert(1, "Amazon")
print(names)

#To remove specific obj
names.pop(0)
print(names)

#To remove last elem
names.pop()
print(names)

#To add @ end
names.append("Facebook")
print(names)

#To remove specific obj
names.remove("Facebook")
print(names)

#To reverse existing list
names.reverse()
print(names)

#To sort all in ascending order
names.sort()
print(names)

#To count total objects that how many times it's repeated
print(names.count("Amazon"))

#To add new list to here
names2=["LinkedIn"]
names.extend(names2)
print(names)

#To clear list
names2.clear()
print(names2)

#To copy into new list
newList=names.copy()
print(newList)

#To find specific obj's index
print(names.index("LinkedIn"))

print(names)

#To get length
print(len(names))

#To check if an obj existing or not
if "LinkedIn" in names:
    print("Yes")

if "Lin" not in names:
    print("Yes")

#To delete
del names[2:]
print(names)

#To add multiple values
#Make sure extenf happens with a list, so put []
names.extend(["Flipkart", "Accenture", "Infosys"])
print(names)

#To find min n max values from numbers
num=[1,2,3,4,5]
print(min(num))
print(max(num))

print(sum(num))