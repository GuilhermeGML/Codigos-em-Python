num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.pop()
for cont in range(0,5):
    num.append(int(input('Digite um valor:')))
print(num)
a = [1, 2, 3, 4]
b = a[:]
b[2] = 5
print(a)
print(b)