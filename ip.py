def is_valid_ip(given_str: str) -> bool:
	if not given_str:
		return False

	given_str_list = given_str.split(".")
	for i in given_str_list:
		if int(i) > 255 or int(i) < 0:
			return False

	if given_str.count(".") != 3:
		return False

	#Не больше 15 символов
	if len(given_str) > 15:
		return False

	# нет пробелов 
	if given_str.count(" ") > 0:
		return False

	#
	for i in given_str:
		if i.isalpha():
			return False

assert is_valid_ip("") == False
assert is_valid_ip("Вася") == False
assert is_valid_ip("192.168.0.1.1") == False, "Больше четырех чисел"
assert is_valid_ip(" 0.2.4.5") == False, "IP не содержит пробелов"
assert is_valid_ip("192.168.0.266") == False, ""