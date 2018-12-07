class bank:

	def add(self):
		us=1
		a=self.acno=input('\n Enter account number:\t')
		b=self.acbal=input('\n Enter account bal\t')
		c=self.acno=raw_input('\n Enter account type:\t')
		d=self.noac=input('\n number of accounts:\t')
		e=self.aname=raw_input('\n name:\t')
		f=self.addre=raw_input('\n address:\t')
		li=[us,a,b,c,d,e,f]
		print li
		
	
x=bank()
x.add()
