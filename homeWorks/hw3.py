class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    def __str__(self):
        return f'{self.__name}:{self.__balance}'


    def moneyx(self):
        money_added = int(input("Enter amount of money to add: "))
        self.__balance += money_added

    def kill(self):
        self.__balance = 0

    def jackpot(self):
        self.__balance *= 10

    def stole_copy(self, other):
        self.__balance += other.__balance



Beka = Bank("Beka", 100)
China = Bank("China", 150)

print("Beka:", Beka._Bank__balance)
print("China:", China._Bank__balance)


kill = Beka.kill()

moneyx = Beka.moneyx()


jackpot = Beka.jackpot()

stole_copy = Beka.stole_copy(other=China)


print("Beka:", Beka._Bank__balance)
print("China:", China._Bank__balance)