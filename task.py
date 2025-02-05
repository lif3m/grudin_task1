# Напишите программу, которая позволяет пользователю управлять информацией о книгах в каталоге.
# Информация о стране – название, столица.
# Программа должна представить пользователю
# следующие возможности:
# 1) Добавить новую страну в каталог
# 2) Найти страну по названию
# 3) Удалить страну из каталога
# 4) Показать информацию о всех странах в каталоге
#       Дополнительные условия:
#       1)При добавлении новой страны:
#       программа проверяет,имеется ли уже такая страна в каталоге.
#       Если да, то программа просит пользователя ввести другие название
#       2) При поиске и удалении страны:
#       программа проверяет, имеется ли такая страна в каталоге.
#       Если нет, то программа сообщает об этом пользователю.

#ключ- название страны
#значение - столица



catalog={
	"Нидерланды":"Амстердам",
    "Андорра":"Андорра-ла-Велья",
    "Греция":"Афины",
    "Сербия":"Белград",
    "Германия":"Берлин",
    "Швейцария":"Берн",
    "Словакия":"Братислава",
    "Бельгия":"Брюссель",
    "Венгрия":"Будапешт",
    "Румыния":"Бухарест",
    "Лихтенштейн":"Вадуц",
    "Мальта":"Валлетта",
    "Польша":"Варшава",
    "Ватикан":"Ватикан",
    "Австрия":"Вена",
    "Литва":"Вильнюс",
    "Ирландия":"Дублин",
    "Хорватия":"Загреб",
    "Украина":"Киев",
    "Молдавия":"Кишинёв",
    "Дания":"Копенгаген",
    "Португалия":"Лиссабон",
    "Великобритания":"Лондон",
    "Словения":"Любляна",
    "Люксембург":"Люксембург",
    "Испания":"Мадрид",
    "Беларусь":"Минск",
    "Монако":"Монако",
    "Россия":"Москва",
    "Норвегия":"Осло",
    "Франция":"Париж",
    "Черногория":"Подгорица",
    "Чехия":"Прага",
    "Исландия":"Рейкьявик",
    "Латвия":"Рига",
    "Италия":"Рим",
    "Сан-Марино":"Сан-Марино",
    "Босния и Герцеговина":"Сараево",
    "Северная Македония":"Скопье",
    "Болгария":"София",
    "Швеция":"Стокгольм",
    "Эстония":"Таллин",
    "Албания":"Тирана",
    "Финляндия":"Хельсинки"
}
print("-"*100)
#цикл для работы с каталогом
while True:
    print('Список возможных действий:')
    print('1 - Добавить навую страну')
    print('2 - Поиск страны по названию')
    print('3 - Удаление страны из каталога')
    print('4 - Показать информацию о всех странах в каталоге')
    print('0 - Закончить работу')
    print("-" * 100)
    # запрашиваем у пользователя номер действия:
    user_choice=int(input("Выберите № действия: "))
    if user_choice==1:
        new_country=input("Введите новую страну: ")
        new_cap=input("Введите ее столицу: ")
        catalog[new_country]=new_cap

    if user_choice==2:
        hide_country=input("Введите страну: ")
        if hide_country in catalog:
            print(catalog[hide_country])
            print("-"*100)


    if user_choice==3:
        del_country=input("Введите страну для удаления: ")
        if del_country in catalog:
            catalog.pop(del_country)
            print(f"Страна {del_country} удалена!")

    if user_choice==4:
        for k,v in catalog.items():
            print(k,v)

    if user_choice==0:
        break
print("Работа окончена! Досвидания...")