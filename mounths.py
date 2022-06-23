mounth = int(input("insert the mounth: "))
if mounth == 2:
      print(f'the count of days of your mounth is equal to: {28}')
elif (mounth <= 7 and mounth % 2 != 0) or (mounth >= 8 and mounth % 2 == 0):
      print(f'the count of days of your mounth is equal to: {31}')

elif (mounth <= 7 and mounth % 2 == 0) or (mounth >= 8 and mount % 2 != 0):
      print(f'the count of days of your mounth is equal to: {30}')
