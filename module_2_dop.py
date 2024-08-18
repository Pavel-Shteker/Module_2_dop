import random

def math_or_death(n):
    result = "" # сначала я хотел сделать список а потом преобразовать его в строку, но сразу записывать в строку оказалось удобнее
    for i in range(1, n): # исключаем 0 и само n
        # print (i)
        for j in range(i+1, n): # исключаем одинаковые пары и зеркала
            print (i, j)
            summary = i + j
            # print (summary) # после второй половины пар, перебор по сути не нужен, но корректно брейк я так и не вставил
            if n % summary == 0:
                result += f"{i}{j}" # очень удобная форма печати, но в лекциях встречалась кажется всего раз, гугл помог
    return result

n = int(random.randrange(3, 20))
at_least = math_or_death(n)
print("Для числа", n, "пароль спасения -", at_least)
