lst = []
lst.append(input("insert name: "))
i = 0
while lst[i] != '':
      lst.append(input("insert name: "))
      i += 1

ind = 0
ind1 = 1
while ind < len(lst):
         if lst[ind] == lst[ind1]:
              lst.remove(lst[ind1])
         ind += 1 
         ind1 += 1 

print(f'your names list is: {lst}') 
