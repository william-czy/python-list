fruits = ["apple", "banana", "cherry"]
print("there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.append("orange")
print("list.append - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.insert(1, "watermelon")
print("list.insert - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.remove("cherry")
print("list.remove - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.sort()
print("list.sort   - there are {} fruits, they are: {}".format(len(fruits), fruits))
