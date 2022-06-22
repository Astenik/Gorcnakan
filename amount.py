def persent(num, per):
     return num * per / 100

def amount(money, per, year):
      """this function returns the amount money  that you put in a bank."""
        i = 1
        while i <= year:
               money += persent(money, per)
               i += 1
        return money


amount_money = int(input("insert the amount of money that you had put in the bank: "))
print(f'the first year your money was: {amount(amount_money, 4, 1)}')
print(f'the second year your money was: {amount(amount_money, 4, 2)}')
print(f'the thired year your money was: {amount(amount_money, 4, 3)}')
