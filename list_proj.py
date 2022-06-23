lst = []
lst.append(input("insert name: "))
i = 0
while lst[i] != '':
      lst.append(input("insert name: "))
      i += 1

for i in range(len(lst)):
        for j in range(len(lst)):
             if lst[i] == lst[j]:
                  delete(lst, j)
  
print(f'your names list is: {lst}')
