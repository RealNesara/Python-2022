'''
#1
fibonacci_numbers = ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34"]
print(fibonacci_numbers)
#2
fav_fruits = ["Apple", "Blueberries", "Bananas", "Orange", "Mango"]
print(fav_fruits)
#3
youtubers = ["PewDiePie", "MrBeast", "UltraFormula1", "Dream"]
print(youtubers)
#4
songs = list()
songs.append("Rasputin")
songs.append("Baby Shark")
songs.append("Smooth Criminal")
songs.append("Red Sun in the Sky")
songs.append("Your Ex-Lover is Dead")
print(songs)
#5

book=[]
book.append(input("Name of a book?\n"))
book.append(input("Name of a book?\n"))
book.append(input("Name of a book?\n"))
book.append(input("Name of a book?\n"))
book.append(input("Name of a book?\n"))
print(book)
'''
#6
print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []
while order_complete == False:
	topping = input("What topping would you like? - push enter to finish")
	if topping == "": 
		print("Order Done")
		order_complete = True
	elif topping in toppings_list:
		print("You already have that topping")
	else: 
		print("Great, adding it to the list")
		toppings_list.append(topping)

print("Here are your toppings")

print(",".join(toppings_list))
'''
#8
names = ["Conor", "Hamish", "Misha", "Noah","Oliver"]
print(names)
'''