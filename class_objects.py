class myclass:
    a = 6
#print(myclass().a)

class person:
    def myfunc(self, name, age):
        self.name = name
        self.age = age
name = input("Enter your name: ")
age = input("ENter your age: ")
p1 = person(name )
print(p1.name)