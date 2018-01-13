from random import randint

def set_number():
	return randint(1, 100)

def set_guess():
	g = input("Take a guess: ")
	return int(g) if g.isnumeric() else set_guess()

def replay():
	r = input("Would you like to play again (y/n)? ")
	if r.isnumeric and len(r) == 1:
		main() if r == 'y' else exit()
	else:
		replay()

def main():
	count = 0
	number = set_number()
	guess = set_guess()
	while guess != number:
		if guess < number:
			count += 1
			print("Too low.")
			guess = set_guess()
		elif guess > number:
			count += 1
			print("Too high.")
			guess = set_guess()
	else:
		count += 1
		print("Great guess! It took you {} guesses.".format(count))
		replay()

main()