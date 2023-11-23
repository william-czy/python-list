fruits = ["banana", "apple", "cherry"]
print("there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.append("orange")
print("list.append  - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.insert(1, "watermelon")
print("list.insert  - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.remove("cherry")
print("list.remove  - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.pop(1)
print("list.pop(1)  - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.sort()
print("list.sort    - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.reverse()
print("list.reverse - there are {} fruits, they are: {}".format(len(fruits), fruits))

fruits.count("apple")
print("list.count   - there are {} apples, they are: {}".format(fruits.count("apple"), fruits))

fruits.clear()
print("list.clear   - there are {} fruits, they are: {}".format(len(fruits), fruits))