obj=1, 1.2, 'str' ,[], {}, True, None
print(type(obj))



def a(b):
    print(b)
a(9)
a(7)
a(8)

class Car:
    name= 'MERS'

    def __init__(self,model, year):
        self.model=model
        self.year=year


    def sayname(self):
        print(self.name)
    def __str__(self):
        return f'{self.name} {self.year}'
    def __len__(self):
        return f'len{self.name} {self.year}'

mers=Car (len('bmw', 1999))
mers2=Car('312', 2010)
print(mers)
print(mers2)