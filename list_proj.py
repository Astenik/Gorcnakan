lst = []
lst.append(input("insert name: "))
i = 0
while lst[i] != '':
      lst.append(input("insert name: "))
      i += 1

for ind in range(len(lst)):
         for ind1 in range(ind + 1, len(lst)):
              if lst[ind] == lst[ind1]:
                       lst.remove(lst[ind1])
          


print(f'your names list is: {lst}') 

