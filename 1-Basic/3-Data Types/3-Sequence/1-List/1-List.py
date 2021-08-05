#Lists are used to store multiple items in a single variable

#Stores in memory sequence like string, we can access through index 0 to n-1

item=["breads", "pasta", "veggies", "pizza"]
print(item[0])

item[1]="Chips"
print(item)
print(item[0:2])


item2=["ABC", "JKL", "XYZ"]
item3=item+item2


item4=[item, item2]
