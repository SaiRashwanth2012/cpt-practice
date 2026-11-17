#Connor and Sai
import random

def player_input(rock):
		return rock

def player_win():
	print("You Won :)")

def bot_win():
	print("Bot wins")

def tie():
	print("You Tied")

running = True

while running:
	answer = input("Want to play a game? (yes/no): ").lower()

	if answer == "no":
		print("Goodbye!")
		running = False
	elif answer == "yes":
		player = player_input(input("Choose Rock, Paper, or Scissors: ").lower())
		list = ["rock", "paper", "scissors"]
		if player not in list:
			print("Please type rock, paper, or scissors.")
			continue

		bot = random.choice(list)
		print()
		print("The Bot chose:", bot)
		print()

		if bot == "rock" and player == "rock":
			tie()
		elif bot == "rock" and player == "paper":
			player_win()
		elif bot == "rock" and player == "scissors":
			bot_win()
		elif bot == "paper" and player == "paper":
			tie()
		elif bot == "paper" and player == "scissors":
			player_win()
		elif bot == "paper" and player == "rock":
			bot_win()
		elif bot == "scissors" and player == "scissors":
			tie()
		elif bot == "scissors" and player == "rock":
			player_win()
		elif bot == "scissors" and player == "paper":
			bot_win()
	else:
		print("Please type yes or no.")