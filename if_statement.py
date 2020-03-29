#here we are going to use if statement

A = float(input("Enter integer or decimal value of A: "))
B = float(input("Enter integer or decimal value of B: "))

if A > B:                  #check the condition and and print accordingly
	print("A is greater than B")
elif A < B:
	print("B is greater than A")
else:
	print("Both numbers are equal")