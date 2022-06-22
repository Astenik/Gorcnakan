def lg(num:int):
      """This function returns the number of lg(num) where num is function argument."""
      if num == 1: 
           return 0
      res = 1
      count = 0
      while res < num:
          res *= 10
          count += 1
      return count

num1 = int(input("insert the firs number: "))
num2 = int(input("insert the second number: "))
print(f'sum of your numbers is equal to: {num1 + num2}')
print(f'subtraction of your numbers is equal to: {num1 - num2}')
print(f'multiplication of your numbers is equal to: {num1 * num2}')
print(f'integer division of your numbers is equal to: {num1 // num2}')
print(f'residual division of your numbers is equal to: {num1 % num2}')
print(f'division of your numbers is equal to: {num1 / num2}')
print(f' lga of your numbers is equal to: {lg(num1)}')
