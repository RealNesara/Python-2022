#1
ice_creams = int(input("How many ice creams do you want?"))
if ice_creams <=20:
	print(f"You wanted {ice_creams} ice creams, we will have that ready in no time.")
else:
	print(f"Sorry but you'll become a fatty if you eat this much!")
#2
fuel = int(input("How far do you need to travel?"))
if fuel <=200:
	print(f"Nice, you can keep driving!")
else:
	print(f"You need to fill up on fuel, immediately!")
#3
age = int(input("What is your age?"))
if age >=18:
	print(f"You are now considered an adult!")
else:
	print(f"You are a minor human.")
#4
fav_movie = input("What is your favourite movie?")
if fav_movie =="Lord of the Rings":
	print(f"You have excellent taste of movies")
else:
	print(f"Sorry, but Lord of the Rings is a better movie!")
#5
question = input("Have you heard of the tale Darth Plagueis the Wise?")
if question =="No":
	print(f"Darth Plagueis is a fictional character in the Star Wars franchise. A Sith Lord with the ability to prevent death and create life, Plagueis is the mentor of Palpatine.")
else:
	print(f"You must be a fan!")
#6
question_2 = input("Who directed Passion of the Christ?")
if question_2 == "Mel Gibson":
	print(f"Correct!")
else:
	print(f"Wrong! Mel Gibson directed the film")
#7
print("Welcome to this quiz. Make sure to USE CAPITAL LETTERS where needed.")
score = 0
quiz_1 = input("What does www stand for in a website browser?").lower()
if quiz_1 =="world wide web":
	print(f"Correct!")
	score= score + 1
else:
	print(f"Wrong! It stands for World Wide Web")
	score= score - 1
quiz_2 = input("What geometric shape is generally used for a stop sign?").lower()
if quiz_2 =="octagon":
	print(f"Correct!")
	score= score + 1
else:
	print(f"Wrong! It's an Octagon")
	score= score - 1
quiz_3 = input("What is the name of the largest ocean on Earth?").lower()
if quiz_3 =="pacific ocean" or quiz_3 == "pacific":
	print(f"Correct!")
	score= score + 1
else:
	print(f"Wrong! It is the Pacific Ocean")
	score= score - 1
quiz_4 = input("What is the rarest M&M colour?").lower()
if quiz_4 =="brown":
	print(f"Correct!")
	score= score + 1
else:
	print(f"Wrong! It's Brown")
	score= score - 1
quiz_5 = input("What was the name of the first soft drink in space?").lower()
if quiz_5 =="coca cola":
	print(f"Correct!")
	score= score + 1
else:
	print(f"Wrong! It's Coca Cola")
	score= score - 1
print(score)