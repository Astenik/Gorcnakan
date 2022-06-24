def day_count(year, month):
      '''This function returns the count of days of the year's month that you give him as arguments.'''
      if year % 4 == 0 and month == 2:
           return 29
      elif year % 4 != 0 and month == 2:
           return 28
      elif (month <= 7 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
            return 31
      elif (month <= 7 and month % 2 == 0) or (month >= 8 and month % 2 != 0):
            return 30
print(f'the count of days of 2022 year 4 month is: {day_count(2022, 4)}')
