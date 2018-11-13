
n = int(raw_input("Enter a number: "))
n2 = int(raw_input("Enter another number: "))

list = [num for num in range(n, n2)]
print(list)
list_2 = [num*2 for num in list]
print(list_2)
