from random import *

# Initialize two empty lists to store random integers
list1 = []
list2 = []

# Ensure lists contain only unique values from the start (redundant here since lists are empty)
list1 = list(set(list1))
list2 = list(set(list2))

def creating():
    # Populate list1 and list2 with 10 random integers each between 0 and 20
    for i in range(10):
        list1.append(randint(0, 20))
    for y in range(10):
        list2.append(randint(0, 20))

def cardinality():
    # Remove duplicate values from list1 and list2 using manual iteration
    # Note: This approach may skip duplicates due to list mutation while iterating
    for n in list1:
        if list1.count(n) > 1:
            list1.remove(n)
    for t in list2:
        if list2.count(t) > 1:
            list2.remove(t)

def biggest():
    # Compare cardinality and display the list with more unique elements
    conc = len(list1) > len(list2)
    if conc:
        print(f'List1 is bigger\n{list1}\n')
        print(f'This is list2\n{list2}')
    else:
        print(f'List2 is bigger\n{list2}\n')
        print(f'This is list1\n{list1}')

# Run all functions when the script is executed directly
if __name__ == '__main__':
    creating()
    cardinality()
    biggest()