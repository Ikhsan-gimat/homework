input_line = input('Введите фруты через запятую:').split(',')

# 1. Спросить у пользователя строку с фруктами через запятую
# (например: “apple, banana, orange, apple, kiwi”)
#и превратить её в список.
#2.Убрать пробелы у каждого фрукта.

split_words = list(input_line)
print(split_words)

# 3. Сделать так, чтобы все фрукты начинались с заглавной буквы
# (Apple, Banana …).

title_words = [word.title() for word in input_line]
print(title_words)

# 4. Убрать повторы с помощью множества (set).

bez_povtor_list =set(input_line)
print(bez_povtor_list)

# 5. Вывести список фруктов в алфавитном порядке.

sorted_words = sorted(split_words, key=lambda word: word.lower())
print(sorted_words)

# 6. Сделать словарь, где: ключ = название фрукта,
# значение = сколько раз он встречался в исходном вводе.

fruit_count = {}
for fruit in input_line:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
    print(fruit_count)

# 7. Найти самый популярный фрукт и вывести его.

maxFruit = ''
maxCount =0
for key, value in fruit_count.items():
    if value > maxCount:
        maxFruit = key
        maxCount = value
print(maxFruit)

# 8. Сделать кортеж из всех уникальных фруктов.

fruit_kortez = tuple(bez_povtor_list)
print(fruit_kortez)

# 9. Проверить, есть ли среди фруктов "Banana", "Mango", "Pineapple".

check_list = ["Banana", "Mango", "Pineapple"]
for f in check_list:
    if f in title_words:
        print('есть в списке')
    else:
        print('нет в списке')

# 10. Спросить у пользователя число N
# и вывести первые N фруктов в алфавитном порядке.

input_line = input('Введите фруты через запятую:').split(',')
split_words = list(input_line)
sorted_words = sorted(split_words, key=lambda word: word.lower())

N = int(input())
print(sorted_words[:N])


