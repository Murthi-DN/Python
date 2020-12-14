#Lists are used to store multiple items in a single variable

#Stores in memory sequence like string, we can access through index 0 to n-1

item=["breads", "pasta", "veggies", "pizza"]
print(item[0])

item[1]="Chips"
print(item)
print(item[0:2])

#Almost same as string but has more few diff methods

item.append("nonveg")
print(item)

#to insert in between
item.insert(1, "fish")
print(item)

#to add 2 lists
item2=["ABC", "JKL", "XYZ"]
item3=item+item2
print(item3)

print(len(item3))

item4=[item, item2]
print(item4)
