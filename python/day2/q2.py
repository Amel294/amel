def grt(n1,n2,n3):
	print("Largest number is")
	if (n1>=n2) and (n1>=n3):
		print(n1)
	elif (n2>=n1) and (n2>=n3):
		print(n2)
	else:
		print(n3)
grt(input("1st\n"),input("2st\n"),input("3st\n"))

