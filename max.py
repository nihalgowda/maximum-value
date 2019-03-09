def func():
	a=int(input ("first number is "))
	b=int(input("second number is "))
	c=int(input("third number is "))
	if a==b and b==c and c==a:
		print("All are same")
	elif a>b and a>c:
		print("First number is greater")
		return
	elif b>a and b>c:
		print("Second number is greater")
		return
	elif c>a and c>b:
		print("third number is greater")
		return
func()