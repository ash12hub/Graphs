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
# traversal_graph = {'0': {'n': ?, 's': ?}}
traversal_graph = {}

# Get exits in starting room
traversal_graph[0] = {}
exits = player.current_room.get_exits()
for exit in exits:
    traversal_graph[0][exit] = '?'

new_room = False
while True:
    if new_room:
        new_room = False
        exits = player.current_room.get_exits()
        for exit in exits:
            if exit not in traversal_graph[player.current_room.id]:
                traversal_graph[player.current_room.id][exit] = '?'

    next_room_found = False            
    for exit in traversal_graph[player.current_room.id]:
        if traversal_graph[player.current_room.id][exit] == '?':
            next_room_found = True
            previous_room = player.current_room
            entrance = ''
            if exit == 'n':
                entrance = 's'
            elif exit == 's':
                entrance = 'n'
            elif exit == 'w':
                entrance = 'e'
            elif exit == 'e':
                entrance = 'w'
            traversal_path.append(exit)
            player.travel(exit)
            traversal_graph[previous_room.id][exit] = player.current_room.id
            if player.current_room.id not in traversal_graph:
                traversal_graph[player.current_room.id] = {}
                traversal_graph[player.current_room.id][entrance] = previous_room.id
                traversal_graph[player.current_room.id]['first_visit'] = entrance
                new_room = True
            break
    
    # Check if all the nodes are found
    # Break out of the supposedly infinite while loop
    if len(traversal_graph) == len(room_graph):
        break
    
    # If no new room found, backtrack
    if not next_room_found:
        prerious_room = player.current_room
        exit = traversal_graph[player.current_room.id]['first_visit']
        traversal_path.append(exit)
        player.travel(exit)
        





# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
#######
