# Здесь определяются функции (сцены квеста), игра запускается на 30 строке
def location_stone():
    print("Подъезжает Илья к трем дорожкам, на перекрестке камень лежит, а на том камне написано:")
    print("Кто вправо поедет – тому убитым быть, кто влево поедет – тому богатым быть, а кто прямо поедет – тому женатым быть»")
    print("1 – Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
    # user_answer для каждой функции свой, его не нужно обнулять
    user_answer = int(input(">>> "))
    if user_answer == 1:
        # Переход на следующий уровень.
        location_killed()
    else:
        location_stone()  # Если пользователь вводит не тот ответ, вызываю функцию заново. TODO: хорошо бы очистить экран


def location_killed():
    print("И поехал он по дороге, где убитому быть. Только он отъехал три версты, напали на него сорок разбойников. Хотят его с коня стащить, хотят его ограбить, до смерти убить.")
    print("1 – Бежать")
    print("2 – Сражаться")
    user_answer = int(input(">>> "))
    if user_answer == 1:
        print(
            "Илья Муромец пришпорил Бурушку, оторвался от разбойников и прискакал к камню.")
        input("ENTER – продолжить")
        location_stone()
    else:
        print("За один взмах десять разбойников лежат, за второй - и двадцати на свете нет! На этом пока все, конец!")


# Квест запускается здесь вызовом функции location_stone(). К этому моменту все функции уже определены.
location_stone()
