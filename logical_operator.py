#logical operators in python

#the following are few examples of using "NOT" logical operator
a = not 2 < 3
print(a)

b = not True
print(b)

x = 129
y = 22
if not x < y:
	print("it worked")

c = not 3 < 2
print(c)



#the following are example(s) of using "AND" logical operator
e = 10
f = 3
if e > 10 and f > 1:
	print("it worked")
else:
	print("You are disobeying 'AND' operator")



#the following are example(s) of using "NAND" logical operator
g = 13
h = 32
if not(g > 14 and h > 54):
	print("it worked")
else:
	print("You are disobeying 'NAND' operator")



#the following are example(s) of using "OR" logical operator
i = 4
j = 23
if i > 1 or j > 34:
	print("it worked")
else:
	print("Both situations dissatisfied by 'OR' operator")




#the following are example(s) of using "NOR" logical operator
i = 4
j = 23
if not(i > 1 or j > 34):
	print("it worked")
else:
	print("The situations is dissatisfied by 'NOR' operator")