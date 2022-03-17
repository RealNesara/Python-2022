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
trap_room = Room("You found a trap room. You lost.")
trap_room = Room("You found a trap room. You died.")

trap_room = Room("You found a trap room. You failed.")
trap_room = Room("You found a trap room. You were found.")

##############################
#DEFINE CONNECTIONS
##############################
jail.north = staffroom
jail.west = library
library.south = hallway
library.west = computer_room
computer_room.west = trap_room
computer_room.north = trap_room
staffroom.north = trap_room
staffroom.east = bathroom
bathroom.south = folder_room
folder_room.east = trap_room

##############################
#DEFINE ITEMS
##############################
door_key_1 = Item("key", "door key", "library key")
key.description = "You look at the key. It is labled library key 1"

door_key_2 = Item("key", "door key", "library key 2")
key.description = "You look at the key. It is labled library key 2"

door_key_3 = Item("key", "door key", "library key 3")
key.description = "You look at the key. It is labled library key 3"

door_key_4 = Item("key", "door key", "computer room key")
key.description = "You look at the key. It is labled computer room"

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
folder_room.items.add(door_key_2)
bathroom.items.add(door_key_3)
library.items.add(door_key_4)
library.items.add(book)
computer_room.items.add(computer)
folder_room.items.add(folder)
jail

##############################
#DEFINE AND VARIABLES
##############################
current_room = jail
inventory = Bag()

##############################
#BINDS (e.g "@when("look"))
##############################
@when("")
def look():
	print(current_room)
	print(f"There are exits, to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)



##############################
#MAIN FUNCTION
##############################