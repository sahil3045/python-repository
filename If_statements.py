# gives condition
a = 5
b = 5

if a>b:
    print(str(a) + " is greater than " + str(b))

if a == b:
    print(str(a) + " is equal to " + str(b))


if a<b:
     print(str(a) + " is lesser than " + str(b))



if a>b:
    print(str(a) + " is greater than " + str(b))
elif a == b:
    print(str(a) + " is equal to " + str(b))
else:
    print((str(a) + " is smaller than " + str(b)))

value = input("Enter the value: ")
if type(value) == str:
    print(value + " is a string.")

else:
    print(value, " is not a str" )

#to check weather a number is divisible by 5
number = int(input("Enter the number: "))
if number%5 == 0:
    print(number, "Is dvisible by 5.")
else:
    print(number, " Is not divisible by 5.")

    