dict={"name":"Google", "year":"1996", "owner": "larry"}

print(d2.get("year"))

d2.pop("owner")

print(dict["name"])

print(d2.items())

print(d2.keys())

print(d2.values())

print(d2.popitem())

print(len(d2))

d2.clear()

dict["location"]="Bengaluru"

del dict["location"]

dict2={'Price': 100}
print(dict.update(dict2))

d2=dict.copy()
