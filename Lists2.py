#adding both lists
fruits = ["Apples", "Mangoes", "Banana", "Apples"]
nos = [1, 3, 5, 4, 2] 
#fruits.extend(nos)
#print(fruits)

#adding a element to a list.
fruits.append("Orange")
print(fruits)
print(len(fruits))

#adding element to a specific position
fruits.insert(2, "Kiwi")
print(fruits)

#removing a element from list
fruits.remove("Kiwi")
print(fruits)
fruits.pop(1)
print(fruits)

#clear a list
#fruits.clear()
#print(fruits)

#to get position of a certain element in a list.
print(fruits.index("Orange"))

#to count the qty of single element.
print(fruits.count("Apples"))

#to make a list ascending.
nos.sort()
print(nos)

fruits.reverse()
print(fruits)

fruits1 = fruits.copy()
print(fruits1)
del fruits1[2]
print(fruits1)


