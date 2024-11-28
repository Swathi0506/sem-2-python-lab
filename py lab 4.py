n = 10  
a = 0
b = 1
print("Fibonacci Series:", end=" ")
if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")

for _ in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
