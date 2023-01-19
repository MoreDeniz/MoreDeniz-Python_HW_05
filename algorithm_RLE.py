# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

my_str = input('Введите строку: ')

if my_str.isalpha():          # состоит ли строка из букв целиком

    new_str = ''
    i = 0
    while i < len(my_str):
        count = 1

        while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
            count += 1
            i += 1
        new_str += str(count) + my_str[i]
        i += 1
    print(new_str)

elif my_str.isalnum():         # состоит ли строка из букв и цифр
    letters = []
    num_string = ""
    for el in my_str:
        if el.isalpha():
            letters.append(el)
            num_string += " "
        else:
            num_string += el

    num_list = num_string.split()   # Получили список из строки с числами
    result = []
    for i in range(len(letters)):
        result.append(letters[i] * int(num_list[i]))
    print("".join(result))