def all_variants(text):
    length = len(text)
    for i in range(1, length + 1):           # i  длинна строки каждой итерации (от 1 до длинны строки)
        for start in range(length - i + 1): # start определяет начальную позицию и конечную
            yield text[start:start + i]     # возвращает индексированую строку (если i = 1, start = 1 выводит: b)


a = all_variants("abc")
for i in a:
    print(i)
# вроде легко, но почему так сложнааа....
