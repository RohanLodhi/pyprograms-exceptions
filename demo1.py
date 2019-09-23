a = 10
b = 0
try:
	c = a/b
except Exception as e:
	c = 0
	print(e)
	#print("Do not Divide by Zero")
	
print("Result is: ",c)

