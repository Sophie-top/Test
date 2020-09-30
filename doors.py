from os import system

# начальная настройка
game = 0
level = 0

#Три двери
while level == 0 and game not in (1, 2, 3):
    system('cls')
    print("У вас револьвер и один патрон. Перед вами три двери")
    g_inv = ["револьвер и один патрон"]
    game = int(input("Что выберете? "))
    if game == 1:
        print("Здесь на вас вылетел рой смертоносных пчел, которые ужалили вас. А что вы хотели?")
        print("Game over")
        level = 1
    elif game == 2:
        print("Здесь были крокодилы. В любом случае вы погибли")
        print("Game over")
        level = 2
    elif game == 3:
        print ("Здесь были волк и лев, которые не ели 2 года.")
        level = 3
    else:("Такой двери нет. Иди в одну из трёх")
else: #нормальный выход из цикла
    game = 0
    print("уровень ", level) #диагностика
    print("игра ", game) #диагностика

#Третья дверь
while level == 3 and game not in (4, 5, 6):
    system('cls')
    level = int(input("Как вы поступите? 4 - застрелиться самому, 5 - застрелить льва, 6 - застрелить волка "))
    if level == 4:
        print("не плохо. game over")
    elif level == 5:
        print ("Ведь лев съел волка.Вы убили льва и выжили. Молодец!")
        print(" The end")
        break
    elif level == 6:
        print("Зачем стрелять в труп? Вас увидел голодный лев. Вы были съедены")
        print("Game Over")
    else:
        print("Такого варианта нет") 