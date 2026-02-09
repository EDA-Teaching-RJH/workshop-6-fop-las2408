#challenge
status = {
    "Power" : 100,
    "Samples" : 0
}

inventory = []

while True:
    try:
        option = (int(input(" Select an option: "\
        "1. Dig for Sample " \
        "2. Report Status " \
        "3. Emergency Stop ")))

        if option == 1:
            name = str(input("Please enter a sample name: "))
            inventory.append(name)
            status["Power"] -= 10
            status["Samples"] += 1

        if option == 2:
            print(status)
            print(inventory)

        if option == 3:
            print("Stopping Now")
            break

    except ValueError:
        print("An option was not selected, please select a valid option...")
        continue