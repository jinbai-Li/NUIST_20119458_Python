import random
num=random.randint(10,20)
while True:
	guess=int(input("a number between 10 and 20"))
	if guess==num:
		print("you are right")
		break

