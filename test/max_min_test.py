# test max & min function

list1 = [1, 3, 4, 6, 7]

a = max(list1, key=lambda x: x%2)
print("a", a)

b = min(list1, key=lambda x: x%2)
print("b", b)

for i in list1:
    print(i%2)

list2 = [1, 1, 0, 0, 1]
print(min(list2))
print(max(list2))
