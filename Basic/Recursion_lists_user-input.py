
n = int(raw_input("Enter a number: "))
n2 = int(raw_input("Enter another number: "))
list = []
for i in range(n, n2):
        list.append(i)
        print(list)
list_2 = []
for j in list:
        list_2.append(j*2)
        print(list_2)
