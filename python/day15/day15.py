import re
def isint():
	iput=str(raw_input("Enter"))
	mo=re.match('.*[0-9].*',iput)
	if mo:
		return True
	else:
		return False
isint()

def isfloat():
	iput=str(raw_input("Enter"))
	mo=re.match('.*[0-9].[0-9].*',iput)
	if mo:
                return True
        else:
                return False


def ishex()
        iput=str(raw_input("Enter"))
        mo=re.match('[r'\s--[0-9a-fa-F]+)(?\s']',iput)
        if mo:
                return True
        else:
                return False











