from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# global dict to hold where we came too and from
reverse = {
    "n": "s", 
    "s": "n", 
    "e": "w", 
    "w": "e"}


def yeet_or_be_yate():

    reversed_traversal_path = []
    # Dict for rooms visited
    visited = {}


    # Build starting room and exits
    visited[player.current_room.id] = player.current_room.get_exits()

    # while loop to keep track of when were get through the length of all the rooms
    while len(visited) < len(room_graph):

        #when we havent visited a room
        if player.current_room.id not in visited:
            #getting the room exits 
            exits = player.current_room.get_exits()
            
            exits.remove(reverse[traversal_path[-1]]) #remove from exits array
            #add to visited
            visited[player.current_room.id] = exits



    return traversal_path





traversal_path = yeet_or_be_yate()

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
