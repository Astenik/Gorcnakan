def is_growing(lst):
        """this function checs if your list growing or not."""
        for ind in range(len(lst)):
              for ind1 in range(ind + 1, len(lst)):
                     if lst[ind] >= lst[ind1]:
                           return False
        return True

def is_decreacing(lst):
        """this function checs if your list decreacing or not."""
        for ind in range(len(lst)):
              for ind1 in range(ind + 1, len(lst)):
                    if lst[ind] <= lst[ind1]:
                           return False
        return True 

lst = [5, 7, 89, 100]
if is_growing(lst) or is_decreacing(lst):
        print("Your list is regulated!")
else:
        print("your list is NOT regulated!")
