#This converts a base 2 number to decimal
n = input('Enter the number: ')
formula = 0
index = len(n)-1
for num in n:
    formula += int(num)*pow(2,index)
    index -=1
print(f'{n} in decimal is {formula}')










