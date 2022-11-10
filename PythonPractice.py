from math import *

name = "Hare Krishna"
num = "108"
print (name.lower().islower())
print (len(num))
print (num[1])
print (name.replace("Krishna", "Rama"))

print (floor(3.9))
print (sqrt(81))

numbers = [1,2,3,4,5]
numbers.insert(0, 2)
numbers.remove(2)
print (numbers)
numbers.clear()
numbers = [1,2,3]
numbers.pop()
print (numbers.count(2))

nums2 = numbers.copy()

name = input("Enter your name: ")
age = input("Enter your age: ")
race = input("Enter your race: ")
print(name + " " + age + " " + race + " " )