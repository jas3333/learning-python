places_visisted = []

def add_place(state, locations, visits):
    locations_visited = {}
    locations_visited["state_visited"] = state
    locations_visited["locations"] = locations
    locations_visited["visits"] = visits
    places_visisted.append(locations_visited)

location_list = []

while True:
    command = input("Commands available: [list], [add], [exit]\n>>> ")
    if command == "exit":
        break
    elif command == "list":
        for visited in places_visisted:
            position = places_visisted.index(visited)
            print(f"{places_visisted[position]}: ")
    elif command == "add":
        which_state = input("Which state did you visit?\n>>> ")
        while True:
            which_locations = input(f"What locations did you visit in {which_state}?\n(Type one entry at a time then hit enter. Type exit to stop adding.)\n>>> ")
            if which_locations == "exit":
                break
            elif which_locations == "":
                print("Not an option")
            else:
                location_list.append(which_locations)
        times_visited = int(input(f"How many times did you visit {which_state}?\n>>> "))
        print("Adding to database...")
        add_place(which_state, location_list, times_visited)
