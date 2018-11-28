#Tupples
tuple1 = (1,2,3,4,5)
stringTuple = ("one","two","tree")
mixedTuple = ("one", tuple1, 3)
itemTuple = ("apple", 2, 3.5)
print(itemTuple)
print("lenght",len(itemTuple))
print("min",min(tuple1))
print("max",max(tuple1))
print("index 2 ",itemTuple.index("apple"))

#Arrays
grocList = ["eggs","milk","flour","butter"]
print(grocList)
print(grocList[1])
print(grocList[2:3])
grocList[1] = "baking soda"
print(grocList)
grocList.append("milk")
print(grocList)
grocList.insert(2,"sugar")
print(grocList)
grocList.remove("butter")
print(grocList)
del grocList[1]
print(grocList)
clothesList = ["tshirt","shorts","sunglasses"]
shoppingList = [grocList,clothesList]
print(shoppingList)
print(shoppingList[1][0])

#Dictionaries
listOfStudents = {0:"Lourenco",1:"Jill",2:"Harry",3:"lucy"}
print(listOfStudents)
print(listOfStudents[0])
listOfStudents[3] = "Tanya"
print(listOfStudents)
print(listOfStudents.keys())
print(listOfStudents.values())

