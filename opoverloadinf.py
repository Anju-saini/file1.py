class Emplloye:
    no_of_leaves =10
    def __init__(self,aname,asaleary,arole):
        self.name= aname
        self.saleary = asaleary
        self.role= arole

    def printdet(self):
        return f" name is {self.name} sealery is {self.saleary}and role is {self.role}"

    @classmethod
    def change_leave(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self, other):#<----------operator overloading
        return self.saleary+other.saleary

    def __truediv__(self, other):#<----------operator overloading
        return self.saleary/other.saleary
    def __mul__(self, other):
        return self.saleary*other.saleary
    def is_(self, other):
        return self.name is other.name
    def __pos__(self):
        return +self.saleary


    def __repr__(self): #<------reper to  show any method details ,call when spcl mention or str no define
        return  f"Employe :'{self.name}' {self.saleary} '{self.role}'"
    def __str__(self):#<------str to  show any data in method, prority more then repr
        return f" name is {self.name} sealery is {self.saleary}  and role is {self.role}"
emp1=Emplloye("anju",455,"programer")
emp2=Emplloye("ashi",555,"haker")
#print(emp1+emp2)#<----------operator overloading
#print(emp1/emp2)#<----------operator overloading
print(emp1*emp2)
print(repr(emp1))
print(emp1 is emp2)
print(emp1)
