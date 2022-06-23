num = []
num.append(int(input("insert numbers: ")))
if num[0] == 0:
     print("Wrong Number")
else: 
         i = 0
         while num[i] != 0:
                num.append(int(input("insert numbers: ")))
                i += 1
         print(f'your list average is: {sum(num) / (len(num) - 1)}')
