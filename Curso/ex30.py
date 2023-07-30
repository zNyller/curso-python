# Duplicates

def duplicated(list):
    s1 = set()
    for n in list:
        if n in s1:
            return n
        s1.add(n)
    return -1

print(duplicated([1, 2, 3, 3, 2, 1]))
print(duplicated([1, 4, 9, 8, 9, 4, 8]))
print(duplicated([4, 7, 1, 2]))