#import all the functions from adventurelib
from adventurelib import *

#rooms
Room.items = Bag()

space = Room("You are drifting in space. You see a spaceship")
airlock = Room("You are in an airlock")
cargo = Room("You are in the cargo bay")
docking = Room("You are in the docking bay")
hallway = Room("You are in the hallway with four exits")
bridge = Room("You are in the bridge of the ship. There is a dead body here")
quarters = Room("You are in the crew quarters. There is a wardrobe on the wall. There is a locker")
mess_hall = Room("You are in the mess hall")
escape_pods = Room("You are in an escape pod")

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.west = airlock
hallway.south = mess_hall
mess_hall.west = airlock
quarters.north = airlock

#items
Item.description = "" #make sure each item has a description
keycard = Item("A red keycard","keycard","card","key","red keycard")
keycard.description = "You look at the keycard and see that it s labelled, Escape pods"

note = Item("A scribbled note","note","paper","code")
note.description = "You look at the note. The number 2,3,5,4 are scribbled"

#add items to room
quarters.items.add(note)

#variables
current_room = space
inventory = Bag()
body_searched = False
used_keycard = False

#binds
@when("jump")
def jump():
	print("You jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else:
		print("There is no air lock here")
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
		print(f"you don't see a {item}")

@when ("inventory")
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == bridge and body_searched == False:
		print("you search the body and a red keycard falls to the floor")
		current_room.item.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("You already searched the body")
	elif:
		print("there is no body here to search")

@when("use ITEM")
def  use(item):
	if itme == keycard and current_room == bridge:
		print("You use the keycardand the escape pod slides open")
		print("The escape pod stands open to the south")
		used_keycard = True
		bridge.south = escape
	else:
		print("you can't use that here")


@when("type code")
def escape_pod_win():
	if not in inventory:
		if current_room == escape:
			print("YOu enter the code and escape. You win")
		else:
			print("there is no where to enter the code")
	else:
		print("You don't have the code. You can't just guess it.")





#EVERYTHING GORS ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

if __name__ == '__main__':
	main()