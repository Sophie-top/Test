print("У вас револьвер и одна пуля. Перед вами три двери, что выберете?")

game = 0
while game not in ("1", "2", "3"):
	if game == 1:
		print("Здесь на вас вылетел рой смертоносных пчел, которые ужалили вас. А что вы хотели?")
		print("Game over")
	elif game == 2:
		print("Здесь были крокодилы. В любом случае вы погибли")
		print("Game over")
	elif game == 3:
		print ("Здесь были волк и лев, которые не ели 2 года. Как вы поступите? 4 - застрелиться самому, 5 - застрелить льва, 6 - застрелить волка")
		if game == 4:
			print("не плохо. game over")
		elif game == 5:
			print ("Ведь лев съел волка. Молодец!")
			print(" The end")
			break
		elif game == 6:
			print("Зачем стрелять в труп?")
			print("Game Over")
else:("Такой двери нет. Иди в одну из трёх, идиот")