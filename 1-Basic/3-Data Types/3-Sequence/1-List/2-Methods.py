names=["IBM", "Microsoft", "Google"]

names.insert(1, "Amazon")
names.remove("Facebook")

names.append("Facebook")
names.pop(0)
names.pop()

names.reverse()
names.sort()

names2=["LinkedIn"]
names.extend(names2)
names.extend(["Flipkart", "Accenture", "Infosys"])

print(len(names))

newList=names.copy()
names2.clear()


print(names.count("Amazon"))
print(names.index("LinkedIn"))


del names[2:]
print(names)


num=[1,2,3,4,5]
print(min(num))
print(max(num))

print(sum(num))



if "LinkedIn" in names:
    print("Yes")

if "Lin" not in names:
    print("Yes")
