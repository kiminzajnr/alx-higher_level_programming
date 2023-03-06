for i in range(0, 100):
	if (i < 10):
		print("0{}".format(i), end=", ")
	elif (i == 99):
		print(i)
		break
	else:
		print(i, end=", ")
	if (i == 99):
		print()
