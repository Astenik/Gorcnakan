def func(tpl):
     m = len(tpl) - 1
     number = 0
     for num in tpl:
          number += num * 10**m 
          m -= 1 
     return number 

tpl = (2, 3, 5)
print(f'number is: {func(tpl)}')
         
