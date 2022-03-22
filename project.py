##############################
#INPORTS
##############################
from adventurelib import *

##############################
#DEFINE BAG
##############################
Room.items = Bag()

##############################
#DEFINE ROOMS
##############################
jail = Room("You are stuck in a rusty cell. You see a dead body and a rusty saw one the floor next to you. ")
library = Room("You are in the library. You see some books on the table. Next to the books is a key.")
folder_room = Room("You are in the folder room. You are surrounded by files. On the table next to a locker there is a key.")

bathroom = Room("You are in the bathroom. There is a key on the floor next to a toilet.")
staffroom = Room("You are in the staffroom. There is a warm cup of coffee on the counter next to it is a flashlight. There is also a newspaper on the chair.")
computer_room = Room("You are in the computer_room. There are rows and rows of computers")

hallway = Room("You are in the hallway. There is a door and the end.")
trap_room_1 = Room("You found a trap room. You lost.")
trap_room_2 = Room("You found a trap room. You died.")

trap_room_3 = Room("You found a trap room. You failed.")
trap_room_4 = Room("You found a trap room. You were found.")

##############################
#DEFINE CONNECTIONS
##############################
jail.north = staffroom
jail.west = library
library.south = hallway
library.west = computer_room
computer_room.west = trap_room_1
computer_room.north = trap_room_2
staffroom.north = trap_room_3
staffroom.east = bathroom
bathroom.south = folder_room
folder_room.east = trap_room_4

##############################
#DEFINE ITEMS
##############################
door_key_1 = Item("key", "door key", "library key")
door_key_1.description = "You look at the key. It is labled library key 1"

door_key_2 = Item("key", "door key", "library key 2")
door_key_2.description = "You look at the key. It is labled library key 2"

door_key_3 = Item("key", "door key", "library key 3")
door_key_3.description = "You look at the key. It is labled library key 3"

door_key_4 = Item("key", "door key", "computer room key")
door_key_4.description = "You look at the key. It is labled computer room"

book = Item("book", "books")
book.description = "You read the book. It has information about why the warehouse shut down. On the second page there seems to be a big blood stain"

computer = Item("computer", "computers")
computer.description = "You sit down at the computer it's already sgined in. On the screen there is a picture of a mand and information below"

folder = Item("folder", "file")
folder.description = "You open one of the folder that reads Misha Shipin. Inside is paper with their information, from their location to where they were born"

rusty_hacksaw = Item("hacksaw", "saw", "rusty hacksaw")
rusty_hacksaw.description = "You reach out and grab the saw. You use it and cut the metal bars, it breaks after you are done "

newspaper = Item("paper", "newspaper", "news")
newspaper.description = "You read the newspaper. There is a police notice on the front page reporting 53 missing people"

flashlight = Item("light", "flashlight", "torch")
flashlight.description = "You grab the flashlight and you trun it on. Surprisingly the flashlight has batteries"

##############################
#ADD ITEMS TO BAGS
##############################
staffroom.items.add(door_key_1)
staffroom.items.add(newspaper)
staffroom.items.add(flashlight)
folder_room.items.add(door_key_2)
bathroom.items.add(door_key_3)
library.items.add(door_key_4)
library.items.add(book)
computer_room.items.add(computer)
folder_room.items.add(folder)
jail.items.add(rusty_hacksaw)

##############################
#DEFINE AND VARIABLES
##############################
current_room = jail
inventory = Bag()

##############################
#BINDS (e.g "@when("look"))
##############################
@when("exit cell")
def exit_cell():
	global current_room
	if current_room == jail:
		print("You exit the jail cell")
		current_room = staffroom
	else:
		print("There is no door here")
	print(current_room)


@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#Checks if the current room list of exits has
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")
	if current_room in [trap_room_1,trap_room_2,trap_room_3,trap_room_4]:
		quit()

@when("look")
def look():
	print(current_room)
	print(f"There are exits, to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when("get ITEM")
@when("take ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into invetory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

@when ("inventory")
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)


@when("look at body")
@when("search body")
def search_body():
	global body_searched
	if current_room == jail and body_searched == False:
		print("You search the body and a wallet falls on to the floor")
		current_room.item.add(picture)
		body_searched = True
	elif current_room == jail and body_searched == True:
		print("You already searched the body")
	else:
		print("There is no body here to search")\

@when("use ITEM")
def  use(item):
	if item == door_key_1 and current_room == library:
		print("You use the key and one of the locks of the door open")
		door_key_1 = True
	else:
		print("You can't use that here")

@when("use ITEM")
def  use(item):
	if item == door_key_2 and current_room == library:
		print("You use the key and one of the locks of the door open")
		door_key_1 = True
	else:
		print("You can't use that here")

@when("use ITEM")
def  use(item):
	if item == door_key_3 and current_room == library:
		print("You use the key and one of the locks of the door open")
		door_key_1 = True
	else:
		print("You can't use that here")




##############################
#MAIN FUNCTION
##############################


def main():
	print(current_room)
	start()
	#start the main loop

if __name__ == '__main__':
	main()