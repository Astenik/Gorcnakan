month = int(input("insert the month: "))
if month == 2:
      print(f'the count of days of your month is equal to: {28} or {29}')
elif (month <= 7 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
      print(f'the count of days of your month is equal to: {31}')

elif (month <= 7 and month % 2 == 0) or (month >= 8 and month % 2 != 0):
      print(f'the count of days of your month is equal to: {30}')
