#challenge.2

command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
]

rover_state = {
    "x": 0,
    "y": 0,
    "samples": 0
}

for command in command_batch:
    word = command.split()
    action = word[0]
    
    if action == "MOVE":
        try:
            # FIX 1: Wrap word[1] in int() so you can add it to the 0 in the dictionary
            rover_state["y"] += int(word[1])
            print("Successful command")
        except:
            print("Error: Invalid distance ignored")

    elif action == "DIG": # FIX 2: Use 'elif' so it doesn't trigger the 'else' below
        # FIX 3: Change command_batch to rover_state
        rover_state["samples"] += 1

    elif action == "TURN": # FIX 2: Use 'elif' here as well
        print("Turning...")
    
    # We added 'elif action == "RETURN": break' so the loop doesn't crash on the last command
    elif action == "RETURN":
        break

    else:
        print("Error: Unknown command sequence")

print(rover_state)













#challenge.1
#status = {
    #"Power" : 100,
    #"Samples" : 0
#}

#inventory = []
#while True:
    #try:
        #option = (int(input(" Select an option: "\
        #"1. Dig for Sample " \
        #"2. Report Status " \
        #"3. Emergency Stop ")))

        #if option == 1:
            #name = str(input("Please enter a sample name: "))
            #inventory.append(name)
            #status["Power"] -= 10
            #status["Samples"] += 1

        #if option == 2:
            #print(status)
            #print(inventory)

        #if option == 3:
            #print("Stopping Now")
            #break

    #except ValueError:
        #print("An option was not selected, please select a valid option...")
        #continue