class employee:

 def add(self):
    self.name=raw_input('\nenter employee name:\t')
    self.nuber=input('\nemployee number:\t')
    self.salary=input('\nenter salary:\t')
 def show(self):
    print('\nname=',self.name,'\n')
    print('e number=',self.nuber,'\n')
    print('salary=',self.salary,'\n')
x=employee()
x.add()
x.show() 
