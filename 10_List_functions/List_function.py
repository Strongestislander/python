
lucky_numbers = [4,8,9,3,6,1,0]
friends = ["tom", "mike", "marculles", "sean", "ashton"]

print(lucky_numbers)
print(friends)
print("\n")

#passes another list into your list
friends.extend(lucky_numbers)
print(friends)
#adds another vaule into the list
friends.append("creed")
print(friends)

#inserts a vaule into the list
friends.insert(1, "kelly")
print(friends)
print(friends)

#removes a vaule from the list
friends.remove("kelly")
print(friends)

print("\n")

#removes everything from the list
friends.clear
friends = ["tom"]
print(friends)

friends = ["tom", "mike", "marculles", "sean", "ashton"]
print(friends)
#pop removes the last element from the list
friends.pop( )
print(friends)
print("\n")

#returns the index vaule of "mike"
print(friends.index("mike"))

friends = ["tom", "mike", "mike", "sean", "ashton"]
print(friends)
#returns how many times the vaule is in the list (mike is in the list twice.
print(friends.count("mike"))
#sorts the list in order
friends.sort()
print(friends)

#copies a list
friends2 = friends.copy()

print(friends2)