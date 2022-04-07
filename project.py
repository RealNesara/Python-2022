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
jail = Room("You are out from the cell. You see a dead body on the floor next to you. The body seems to have something in it's pocket. ")
library = Room("You are in the library. You see some books on the table. There is also a door to the west but it's locked.")
folder_room = Room("You are in the folder room. You are surrounded by folders. On the table next to a locker there is a rusty key labeled library 3 .")

bathroom = Room("You are in the bathroom. There is a silver key on the floor next to a toilet.")
staff_room = Room("You are in the staff room. There is a warm cup of coffee on the counter next to it is a flashlight. There is also a newspaper on the chair with a golden key labeled library key 2.")
computer_room = Room("You are in the computer room. There are rows and rows of computers. There is one laptop on the desk. It is on but it requires a pin to login.")

hallway = Room("You are in a dark room. You can't see anything")
trap_room_1 = Room("You found a trap room. You lost.")
trap_room_2 = Room("You found a trap room. You died.")

trap_room_3 = Room("You found a trap room. You failed.")
trap_room_4 = Room("You found a trap room. You were found.")
jail_cell = Room("You are stuck in a cell. There is a rusty saw on the floor next to you. You have been kidnapped by a serial killer, break out and escape before you get found. Make sure you get evidence to show the police. Be aware that there will be death rooms that will kill you if you run in to them.")

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

rusty_saw = Item("rusty saw", "saw")
rusty_saw.description = "You grab the saw. It is covered it rust and is slowly disintegrating in your hand"

laptop = Item("laptop", "computer")
laptop.description = "You sit down at the laptop it needs a pin to login."

folder = Item("folder", "file")
folder.description = "You open one of the folder that reads Misha Shipin. Inside is paper with their information, from their location to where they were born"

newspaper = Item("paper", "newspaper", "news")
newspaper.description = "You read the newspaper. There is a police notice on the front page reporting 53 missing people"

flashlight = Item("light", "flashlight", "torch")
flashlight.description = "You grab the flashlight and you turn it on. Surprisingly the flashlight has batteries"

key_card = Item("pass", "pin", "key card", "card", "keycard")
key_card.description = "You look at the key card it reads 73923"

warm_coffee = Item("coffee", "warm coffee", "cup of coffee","cup")
warm_coffee.description = "You smell the coffee it smell suspicious. Don't consume it."

dead_body = Item("body", "dead body", "man", "dead man")
dead_body.description = "You see a dead man on the ground. It seems to have been stabed to death."


##############################
#ADD ITEMS TO BAGS
##############################
staff_room.items.add(golden_key)
staff_room.items.add(newspaper)
staff_room.items.add(flashlight)
folder_room.items.add(rusty_key)
bathroom.items.add(silver_key)
library.items.add(book)
computer_room.items.add(laptop)
folder_room.items.add(folder)
#jail.items.add(key_card)
jail_cell.items.add(rusty_saw)
staff_room.items.add(warm_coffee)
jail.items.add(dead_body)

##############################
#DEFINE AND VARIABLES
##############################
current_room = jail_cell
inventory = Bag()
rusty_key_used = False
silver_key_used = False
golden_key_used = False
body_searched = False
key_card_used = False
rusty_saw_used = False
used_warm_coffee = False

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

@when("eat body")
@when("eat")
def eatbody():
	if current_room == jail:
		print("You eat the dead man. You died because of bad ideas.")
		quit()


@when("use ITEM")
def  use(item):
	global rusty_key_used,silver_key_used,golden_key_used,current_room
	if item in inventory and current_room == library and item == "rusty key":
		print("You use the rusty key and one of the locks of the door open")
		rusty_key_used = True
	
	elif item in inventory and current_room == library and item == "golden key":
		print("You use the golden key and one of the locks of the door open")
		golden_key_used = True
	
	elif item in inventory and current_room == library and item == "silver key":
		print("You use the silver key and one of the locks of the door open")
		silver_key_used = True

	elif rusty_key_used == True and silver_key_used == True and golden_key_used == True:
		print("You enter the final key and it unlocks a door to the west")
		library.west = computer_room
	
	elif item in inventory and current_room == hallway and item == "flashlight":
		print("You turn on the flashlight. The room quickly lights up revealing a long hallway with a door to the east.")
		hallway.description = "It's too dark here"
	
	elif item in inventory and current_room == jail_cell and item == "saw":
		print("You use the saw. It cuts the bars of the cell and lets you out but it broke")
		current_room = jail
		print("you climb through the cell bars and are now in the jail room")
		print(current_room)		
	else:
		print("You can't use that here")

@when("read ITEM")
@when("look at ITEM")
def  read(item):
	if item in inventory and current_room == folder_room and item == "folder":
		print("You open one of the folder that reads Misha Shipin. Inside is paper with their information, from their location to where they were born")
		used_folder = True

	elif item in inventory and current_room == staff_room and item == "newspaper":
		print("You read the newspaper. There is a police notice on the front page reporting 53 missing people and 73 dead bodies")
		used_newspaper = True

	elif item in inventory and current_room == library and item == "book":
		print("You read the book. It has information about why the warehouse shut down. On the second page there seems to be a big blood stain")
		used_books = True

	elif item in inventory and current_room == jail and item == "key card":
		print("You look at the key card. It has a pin that reads 73923 ")

		
@when("drink ITEM")
@when("lick ITEM")
@when("eat ITEM")
def drink(item):
	if item in inventory and current_room == staff_room and item == "coffee":
		print("You smell the coffee it smell suspicious. You drink the coffee, it runs down you digestive system and burns you from the inside. You died")
		used_warm_coffee = True
		quit()

	elif item in inventory and current_room == library and item == "book":
		print("You lick the blood stain. You died because of blood poisoning.")
		quit()

	elif item in current_room == jail and item == "dead body":
		print("You eat the dead man. You died because of bad ideas.")
		quit()
	
	elif item in inventory and current_room == staff_room and item == "golden key":
		print("You eat the golden key. Kind of hard to solaw buy you fight through it. You died because of digestive problems.")
		quit()

	elif item in inventory and current_room == bathroom and item == "silver key":
		print("You eat the silver key. Kind of hard to solaw buy you fight through it. You died because of digestive problems.")
		quit()

	elif item in inventory and current_room == folder_room and item == "rusty key":
		print("You eat the rusty key. Kind of hard to solaw buy you fight through it. You died because of digestive problems.")
		quit()

@when("")
	elif item in inventory and current_room == staff_room and item == "light"



@when("enter password")
@when("enter pin")
@when("enter pass")
def computer_room_win():
	if len(inventory)<10:
		print("You need more evidence to show the police. Get more items.")
		return
	if "keycard" not in inventory:
		if current_room == computer_room:
			print("You enter the code and escape. You win :)")
	else:
		print("There is no where to enter the code")
		print("You don't have the code. You don't know numbers so you can't guess it.")
		quit()


@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == jail and body_searched == False:
		print("You search the body and a card falls to the floor. There is a pin written on it.")
		jail.items.add(key_card)
		body_searched = True
	elif current_room == jail and body_searched == True:
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