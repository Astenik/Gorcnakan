month = input("insert month name: ")
day = int(input("insert the day: "))
if day >= 31:
      print("your day is not accurate")
elif month in ('December', 'January', 'February'):
      print("it is Winter")

elif month in ('March', 'April', 'May'):
       print("it is Spring")

elif month in ('June', 'July', 'August'):
      print("it is Summer")

elif month in ('September', 'October', 'November'):
      print("it is Autumn")
