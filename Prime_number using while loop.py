


number = int(input("Enter a number: "))

Condition = False

while number > 1:
    for i in range(2, number):
        if(number % i == 0):
            Condition = True
            break

if Condition:
    print(f"{number} is a not prime number")
else:
    print(f"{number} is a prime number")