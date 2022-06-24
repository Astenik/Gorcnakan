def max_min(lst):
      maxim = lst[0]
      minim = lst[0]
      for num in lst:
           if num > maxim:
               maxim = num
           if num < minim:
               minim = num
      summ = maxim + minim
      return summ

lst = [2, 4, 45, 9, 1]
print(f'sum of max and min is equal to: {max_min(lst)}')
