#1.1
print("Hello, World!")
#1.2
if 5 > 2:
 print("YES")

#2.1
#This is a comment
#2.2
"""
This is a comment
written in 
more than just one line
"""

#3.1
carname = "Volvo"
#3.2
x = 50
#3.3
x = 5
y = 10
print (x + y)
#3.4
x = 5
y = 10
z = x + y
print (z)
#3.5
x, y, z = "Orange", "Banana", "Cherry"
#3.6
x = y = z = "Orange"
#3.7
def myfunc():
global x
  x = "fantastic"

#4.1
x = 5
print(type(x))
int
#4.2
x = "Hello World"
print(type(x))
str
#4.3
x = 20.5
print(type(x))
float
#4.4
x = ["apple", "banana", "cherry"]
print(type(x))
list
#4.5
x = ("apple", "banana", "cherry")
print(type(x))
tuple
#4.6
x = {"name" : "John", "age" : 36}
print(type(x))
dict
#4.7
x = True
print(type(x))
bool

#5.1
x = 5
x = float(x)
#5.2
x = 5.5
x = int(x)
#5.3
x = 5
x = complex(x)

#6.1
x = "Hello World"
print(len)
#6.2
txt = "Hello World"
x = txt[0]
#6.3
txt = "Hello World"
x = txt[2:5]
#6.4
txt = " Hello World "
x = txt.scrip()
#6.5
txt = "Hello World"
txt = txt.upper()
#6.6
txt = "Hello World"
txt = txt.lower()
#6.7
txt = "Hello World"
txt = txt.replace(H, J)
#6.8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
