fruits = ["apple", "banana", "cherry"]
print("there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.append("orange")
print("there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.insert(1, "watermelon")
print("there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.remove("cherry")
print("there are {} fruits, they are: {}".format(len(fruits), fruits))


fruits.sort()
print("there are {} fruits, they are: {}".format(len(fruits), fruits))