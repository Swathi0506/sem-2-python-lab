print("Enter'c' to convert from celsius to Fahrenheit")
print("Enter 'f' to convert from fahrenheit to celsius")
choice=input("Enter your choice:")
if choice == 'c':
    celsius = float(input("Enter temperature in celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print('%2f celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
elif choice == 'f':
    fahrenheit = float(input("Enter temperature in fahrenheit:"))
    celsius = (fahrenheit -32) * 5/9
    print('%.2f Fahrenheit is: %0.2f celsius' %(fahrenheit, celsius))
else:
    print('Invalid Input')
