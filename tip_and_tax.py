def percent(bill:float, n:int):
      """this function returns the n percent os bill"""
      return bill * n / 100
  
bill = float(input("insert the amount of your bill: "))
print(f'the tip is equal to: {percent(bill, 18):f2} $')
print(f'the tax is equal to: {percent(bill, 20):f2} $')
print(f'the bill is equal to: {bill:f2} $')



