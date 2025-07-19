def conversion():
    no =input('Enter the number: ')
    formula = 0
    index = len(no)-1
    for num in no:
        formula += int(num)*pow(2,index)
        index -=1
    print(formula)
conversion()