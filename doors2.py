def door_1():
    print("Здесь на вас вылетел рой смертоносных пчел, которые ужалили вас. А что вы хотели?")
    print("Game over")
    


def door_2():
     print("Здесь были крокодилы. В любом случае вы погибли")
     print("Game over")


def door_31():
    print("не плохо. game over")
    if game == 4:


def  door_32():
     print ("Ведь лев съел волка.Вы убили льва и выжили. Молодец!")
     print(" The end")


def door_33():
     print("Зачем стрелять в труп? Вас увидел голодный лев. Вы были съедены")
     print("Game Over")


def door_3():
    print ("Здесь были волк и лев, которые не ели 2 года.")
    game = int(input("Как вы поступите? 4 - застрелиться самому, 5 - застрелить льва, 6 - застрелить волка "))
    if game == 4:
       door_31()
    elif game == 5:
        door_32()
    elif game == 6:
       door_33()
    else:
        print("Такого варианта нет") 


def doors():
     print("У вас револьвер и один патрон. Перед вами три двери")
     game = int(input("Что выберете? "))
     if game == 1:
         door_1()
     elif game == 2:
         door_2()
     elif game == 3:
         door_3()
     else:("Такой двери нет. Иди в одну из трёх")
