import abc
class Employee :
    __metaclass__=abc.ABCMeta   
    def __init__(self,pname,pno,pby):
        self.name=pname
        self.no=pno
        self.basic=pby
        self.da=.3*self.basic
        self.hra=.1*self.basic
        self.spa=0
       # self.salary=self.basic
    @abc.abstractmethod
    def calcSpa(self):
        pass
    @abc.abstractmethod
    def calcHra(self):
        pass
    def calcSal(self):
        self.salary=self.basic+self.da+self.hra+self.spa
    def disp(self):
        self.calcHra()
        self.calcSal()
        print 'name :%s,empno:%d,Net salary:%f'%(self.name,self.no,self.salary)
           
class Engineer(Employee):
    def calcSpa(self):
        self.spa=0.2*self.basic           
           
class Officer(Employee):
    def calcSpa(self):
        self.spa=0.1*self.basic
    def calcHra(self):
        self.hra=.1*self.basic
           
class  JEngineer(Engineer):
    def calcHra(self):
        self.Hra=self.hra+500

class  SEngineer(Engineer):
    def calcHra(self):
        self.Hra=self.hra+1000
sEng=SEngineer('varun',101,70000)
jEng=JEngineer('chinnu',102,55000)
off =Officer('amal',102,990000)
sEng.disp()
jEng.disp()
off.disp()
