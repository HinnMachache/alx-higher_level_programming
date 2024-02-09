#!/usr/bin/python3
# 0-main.py
lookup = __import__("0-lookup").lookup

class Testclass1:
    pass

class Testclass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("My name is {} and I'm {} year(s) old.".format(self.name, self.age))


object1 = Testclass1()
object2 = Testclass2("Hinn", 20)
# print(lookup(object1))
# print(lookup(object2))
print(lookup(int))
