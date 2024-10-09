class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
            self.__name = value
    @property
    def balance(self):
      return self.__balance
    @balance.setter
    def balance(self, value):
        self.__balance = value

    def moneyX(self, money):
        self.balance += money
        return self.balance

    def kill (self):
        self.balance = 0
        return self.balance

    @property
    def kill(self):
        return self._kill()

    def __jackpot(self):
     self.balance = self.balance * 10
     return self.balance

    @property
    def jackpot(self):
        return self.__jackpot()

    def __add2balances(self, name):
        self.balance += name.balance
        return self.balance

    @property
    def add2balances(self):
        return self.__add2balances()

x = int(input("Введите число: "))
bank= Bank ("Visa", 3333)
print(bank.moneyX(x))
bank2 = Bank ("Mbank", 9999)
print(bank2.add2balances(bank2.name))


class Calculator:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2= num2
    def __sub__(self):
        return self.num1-self.num2
    def __add__(self):
        return self.num1+ self.num2
    def __mul__(self):
        return self.num1 * self.num2
    def __truediv__(self):
        return self.num1 / self.num2
num1= int(input("Введите первое число"))
num2= int(input("Введите второе число"))
action= input("Введите действие")
calc= Calculator(num1, num2)
calc = Calculator (numi, num2)
if action == "*":
    print (calc.__mul__())
elif action == "-":
    print (calc.__sub__())
elif action == "+":
    print (calc.__add__())
elif action == "/":
    print (calc.__truediv__())
