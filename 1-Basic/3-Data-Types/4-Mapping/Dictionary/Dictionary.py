dict={"name":"Google", "year":"1996", "owner": "larry"}
d2=dict.copy()
print(d2)

#To remove obj by key
d2.pop("owner")
print(d2)

#To get obj by key
print(d2.get("year"))
print(dict["name"])

#To list keys n values
print(d2.items())
print(d2.keys())
print(d2.values())

#To remove last obj
print(d2.popitem())

#To get length
print(len(d2))

#To clear
d2.clear()
print(d2)

#To add value
print(dict)
dict["location"]="Bengaluru"
print(dict)

#To delete by del method
del dict["location"]
print(dict)

#To add other dict
dict2={'Price': 100}
print(dict.update(dict2))
print(dict)