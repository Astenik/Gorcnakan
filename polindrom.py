def is_polindrom(n):
        lst = []
        i = 0
        while i < len(n):
             string = ' '
             if (n[i] >= 'a') and (n[i] <= 'Z'):
                    string += n[i]
             else:
                   lst.append(string)
             i += 1  
        rev_lst = [None]*len(lst)
        ind = 0
        ind1 = len(lst) - 1 
        while ind1 >= 0:
             rev_lst[ind] = lst[ind1]
             ind += 1 
             ind1 -= 1 
        if lst == rev_lst:
              return True
        return False

sentenses = input("insert the sentence: ")
print(f'is tour sentence polindrom? {is_polindrom(sentenses)}')
