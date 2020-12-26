import my_classes as mc

def main():
    global player
    player = mc.Player("Василий", "Бескровный", 1, 100)
    player.print_stats()

    def fight():

        def create_enemy():
            global enemy
            enemy = mc.Enemy(1)
            enemy.print_stats()

        def battle(player, enemy):
            while player.HP < 0 or enemy.HP < 0:
                enemy.change_stats(1)
                print()

        create_enemy()
        battle(player, enemy)
    fight()

main()
