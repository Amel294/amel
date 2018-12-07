import re
yourString=input()
	number = re.search(r'\d+', yourString).group()
	if number==True:
		print("Correct")
	else:
		print("Incorrect")
