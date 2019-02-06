

import random
print('...rock....')
print('...paper...')
print('...scissors...')
e = True
while e == True:
	a = ['rock', 'paper', 'scissors']
	b = input("Please enter a choice: ").lower()
	c = random.choice(a)
	if b in a:

		if (b == 'rock' and c == 'scissors') or (b == 'scissors' and c == 'paper') or (b == 'paper' and c == 'rock'):
			print("The computers's choice is " + c)
			print("You Win")
			e = False

		elif (b == 'scissors' and c == 'rock') or (b == 'paper' and c == 'scissors') or (b == 'rock' and c == 'paper'):
			print(c)
			print("You Lose")
			e = False
		else:
			print(c)
			print("Draw throw again!")
	else:
		print("That is not a choice! Try Again!")