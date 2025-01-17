#1
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print("Sum of all items:", total)

#2
rows = int(input())
for i in range(1, rows + 1):  
    for j in range(i):       
        print(i, end=" ")    
    print()                  

