import sys
from time import *
while True:
    eqn = input("Enter the equation [q to quit]: ")
    if eqn.lower() == 'q':
        break
    try:
        if '+' in eqn:
            numbers = eqn.split('+')
            result = sum(int(num.strip()) for num in numbers)
            print("\nAdding", end="", flush=True)
            for i in range(6):
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(0.5)
            print("\n")
            sleep(1)
            print(f'={result}')

        elif '-' in eqn:
            numbers = eqn.split('-')
            result = int(numbers[0].strip())
            for num in numbers[1:]:
                result -= int(num.strip())
            print("\nSubtracting", end="", flush=True)
            for i in range(6):
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(0.5)
            print("\n")
            sleep(1)
            print(f'={result}')
        elif '*' in eqn:
            numbers = eqn.split('*')
            result = 1
            for num in numbers:
                result *= int(num.strip())
            print("\nMultiplying", end="", flush=True)
            for i in range(6):
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(0.5)
            print("\n")
            sleep(1)
            print(f'={result}')
        elif '/' in eqn:
            numbers = eqn.split('/')
            result = int(numbers[0].strip())
            for num in numbers[1:]:
                divisor = int(num.strip())
                if divisor == 0:
                    raise ZeroDivisionError("You can't divide by zero.")
                result /= divisor
            print("\nDividing", end="", flush=True)
            for i in range(6):
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(0.5)
            print("\n")
            sleep(1)
            print(f'={result}')

        else:
            print("Operator not supported yet.")
    except ValueError:
        print("Invalid input. Make sure to only use numbers and valid operators.")
    except ZeroDivisionError as e:
        print(e)

