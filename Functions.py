def greetings_function(name):
    print("Welcome " + name + " !!")
    #it can only take string and not integer because it does not concatenate for using it use str(name)
greetings_function("Sahil")


def add_func(a, b):
    print(a+b)
a = int(input("Enter a number: "))
b = int(input("ENter the number to add: "))
add_func(a, b)

def greetings_function(*names): #* means user can input many names 
    print("Welcome " + names[2] + " !!")
greetings_function("Sahil", "Ram", "Tom")

#return 
def add_funct():
    return 9+6
print(add_funct())

def add_functi(a, b):
    return a+b
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(add_functi(a, b))