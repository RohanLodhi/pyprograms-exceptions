a = 10
b = 0
c = 0
try:
	c = a/b
	#print("Do not Divide by Zero")
except ZeroDivisionError as s:
	print(s)
	
except Exception as e:
	c = 0
	print(e)

print("Result is: ",c)

