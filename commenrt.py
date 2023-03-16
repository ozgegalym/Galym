commentators = {} # создаем пустой словарь для хранения комментаторов
while True:
    comment = input() # считываем комментарий
    if comment == "": # если введена пустая строка, выходим из цикла
        break
    name,text= comment.split(":") # разделяем имя и текст комментария по символу ":"
    name = name.strip() # убираем возможные пробелы в начале и конце имени
    commentators[name] = True # добавляем имя комментатора в словарь

# выводим на экран общее число уникальных комментаторов
print(len(commentators))