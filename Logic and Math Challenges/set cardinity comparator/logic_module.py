from random import randint

list1 = []
list2 = []

def creating(entry1, entry2):
    list1.clear()
    list2.clear()
    for i in range(10):
        list1.append(randint(0, 20))
    for y in range(10):
        list2.append(randint(0, 20))
    entry1.delete(0, 'end')
    entry1.insert(0, str(list1))
    entry2.delete(0, 'end')
    entry2.insert(0, str(list2))

def cardinality():
    global list1, list2
    list1 = list(set(list1))
    list2 = list(set(list2))

def biggest():
    if len(list1) > len(list2):
        return f"List1 has more unique values:\n{list1}"
    elif len(list2) > len(list1):
        return f"List2 has more unique values:\n{list2}"
    else:
        return f"Both lists have equal unique values:\nList1: {list1}\nList2: {list2}"