number = int(input("Enter your number: "))

if number < 2:
    print(f"{number} is not a prime number")
else:
    for n in range(2, number):
        if number % n == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")