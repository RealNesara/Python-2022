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
jail = Room("You are in a rusty cell. You see a dead body on the floor next to you. ")
library = Room("You are in the library. You see some books on the table.")
folder_room = Room("You are in the folder room. You are surrounded by files. On the table next to a locker there is a rusty key labeled library 3 .")

bathroom = Room("You are in the bathroom. There is a silver key on the floor next to a toilet.")
staff_room = Room("You are in the staff room. There is a warm cup of coffee on the counter next to it is a flashlight. There is also a newspaper on the chair with a golden key labeled library key 2.")
computer_room = Room("You are in the computer room. There are rows and rows of computers")

hallway = Room("You are in a dark room. You can't see anything")
trap_room_1 = Room("You found a trap room. You lost.")
trap_room_2 = Room("You found a trap room. You died.")

trap_room_3 = Room("You found a trap room. You failed.")
trap_room_4 = Room("You found a trap room. You were found.")

##############################
#DEFINE CONNECTIONS
##############################
jail.north = staff_room
jail.west = library
library.south = hallway
hallway.east = folder_room 
#library.west = computer_room #will add in later because it starts locked
computer_room.west = trap_room_1
computer_room.north = trap_room_2
staff_room.north = trap_room_3
staff_room.east = bathroom
bathroom.south = folder_room
folder_room.east = trap_room_4

##############################
#DEFINE ITEMS
##############################
rusty_key = Item("rusty key", "library key")
rusty_key.description = "You look at the rusty key. It is labeled library key 1"

golden_key = Item("golden key", "library key 2")
golden_key.description = "You look at the golden key. It is labeled library key 2"

silver_key = Item("silver key", "library key 3")
silver_key.description = "You look at the silver key. It is labeled library key 3"

book = Item("book", "books")
book.description = "You read the book. It has information about why the warehouse shut down. On the second page there seems to be a big blood stain"

computer = Item("computer", "computers")
computer.description = "You sit down at the computer it's already signed in. On the screen there is a picture of a man and information below"

folder = Item("folder", "file")
folder.description = "You open one of the folder that reads Misha Shipin. Inside is paper with their information, from their location to where they were born"

newspaper = Item("paper", "newspaper", "news")
newspaper.description = "You read the newspaper. There is a police notice on the front page reporting 53 missing people"

flashlight = Item("light", "flashlight", "torch")
flashlight.description = "You grab the flashlight and you turn it on. Surprisingly the flashlight has batteries"

key_card = Item("pass", "pin")
key_card.description = "You look at the key card it reads 73923"


##############################
#ADD ITEMS TO BAGS
##############################
staff_room.items.add(golden_key)
staff_room.items.add(newspaper)
staff_room.items.add(flashlight)
folder_room.items.add(rusty_key)
bathroom.items.add(silver_key)
library.items.add(book)
computer_room.items.add(computer)
folder_room.items.add(folder)
jail.items.add(key_card)

##############################
#DEFINE AND VARIABLES
##############################
current_room = jail
inventory = Bag()
rusty_key_used = False
silver_key_used = False
golden_key_used = False
body_searched = False

##############################
#BINDS (e.g "@when("look"))
##############################

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
	if current_room == hallway:
		print("It's too dark to see here")
		return
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
	#put into inventory
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



@when("use ITEM")
def  use(item):
	global rusty_key_used,silver_key_used,golden_key_used
	if item in inventory and current_room == library and item == "rusty key":
		print("You use the rusty key and one of the locks of the door open")
		rusty_key_used = True
	
	elif item in inventory and current_room == library and item == "golden key":
		print("You use the golden key and one of the locks of the door open")
		golden_key_used = True
	
	elif item in inventory and current_room == library and item == "silver key":
		print("You use the silver key and one of the locks of the door open")
		silver_key_used = True
	else:
		print("You can't use that here")

	if rusty_key_used == True and silver_key_used == True and golden_key_used == True:
		print("You enter the final key and it unlocks a door to the west")
		library.west = computer_room
	elif item in inventory and current_room == hallway and item == "flashlight":
		print("You turn on the flashlight. The room quickly lights up revealing a long hallway with a door at the end.")
		hallway.description = "It's too dark here"
	

@when("read ITEM")
@when("look at ITEM")
def  read(item):
	if item in inventory and current_room == folder_room and item == "folder":
		print("You open one of the folder that reads Misha Shipin. Inside is paper with their information, from their location to where they were born")
		used_folder = True

	elif item in inventory and current_room == staff_room and item == "newspaper":
		print("You read the newspaper. There is a police notice on the front page reporting 53 missing people and 73 dead bodies")
		used_newspaper = True

	elif item in inventory and current_room == library and item == "books":
		print("You read the book. It has information about why the warehouse shut down. On the second page there seems to be a big blood stain")
		used_books = True


@when("enter password")
@when("enter pin")
@when("enter pass")
def computer_room_win():
	if item in inventory and current_room == computer_room and item == "key_card":
		print("You enter the code and escape. You win")
	else:
		print("there is no where to enter the code")
		print("You don't have the code. You can't just guess it.")


@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == jail and body_searched == False:
		print("You search the body and a key card falls to the floor")
		current_room.item.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("You already searched the body")
	else:
		print("There is no body here to search")



##############################
#MAIN FUNCTION
##############################


def main():
	print(current_room)
	start()
	#start the main loop

if __name__ == '__main__':
	main()