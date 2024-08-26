first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

list_c = zip(first, second)

b = [len(i)-len(j) if len(i) > len(j) else len(j)-len(i) for i,j in list_c if len(j) != len(i)]
d = []
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(b)
print(list(second_result))
