from random import randint as random
from pathlib import Path

print("KingNullboy's Python Number Guessing Game")

while True:
	num = random(1,100)
	guess = -1
	file = Path("save.txt")
	if not file.exists() or file.st_size == 0:
		file.touch()
		file.write_text("0,0")
	
	plays, wins = map(int, file.read_text().split(","))
	plays += 1

	print(f"You have played this game {plays-1} time{'' if plays-1 == 1 else 's'}, and won it {wins} of those times for a total win rate of {wins/max(1,plays-1)*100}%.")
	
	while num != guess:
		try:
			guess = int(input("What is your guess of the secret number? (1-100)\n> "))
		except ValueError:
			print("Buddy, that's not a number. Defaulting to 50.")
			guess = 50

		if guess < 1 or guess > 100:
			print("That's not a number between 1 and 100. Can't you read?")
		elif guess > num:
			print("That number is greater than the secret number.")
		elif guess < num:
			print("That number is less than the secret number.")
		elif guess == num:
			print("You win!")
			wins += 1
			file.write_text(f"{plays},{wins}")

	while True:
		again = input("Play again? (Y/n)\n> ")
		if not (again.lower().startswith("y") or again.lower().startswith("n")):
			print("That doesn't start with yes or no. Can't you read?")
			continue
		break
	if again.lower().startswith("y"):
		continue
	else:
		break