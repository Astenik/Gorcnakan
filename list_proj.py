lst = []
lst.append(input("insert name: "))
i = 0
while lst[i] != '':
      lst.append(input("insert name: "))
      i += 1
for num in lst:
            for num1 in lst:
                  if num == num1:
                        lst.remove(num1)


print(f'your names list is: {lst}') 
