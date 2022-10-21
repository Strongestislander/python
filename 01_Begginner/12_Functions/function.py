#defines a function
def say_hi():
    print("Hello user: ")
#calls the function
say_hi()

#calls the function with a parameter called "name"
print("\n")
def say_hi(name):
    print("Hello: " + name)

say_hi("john")
say_hi("Mike")

#calls the function with two parameters one for age and name.
print("\n")
def say_hi(name, age):
    print("Hello: " + name + " you are " + str(age))

say_hi("john", 50)
say_hi("Mike", 32)