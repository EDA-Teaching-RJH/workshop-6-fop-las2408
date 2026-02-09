#3.2

def get_coordinate():
    while True:
        try:
            coord = int(input("Please enter an x coordinate: "))
        except ValueError:
            print("Invalid coordinate")
            continue
        else:
            break
        return coord
    
    print(coord)

get_coordinate()
#while True:
        #try:
               #motor_speed = int(input("Enter Motor Speed: "))
        #except ValueError:
            #print("Error: Corrupted Signal. Maintaining current speed.")
            #continue
        
        #else:
              #print(f"Speed set to {motor_speed}")
              #break

            
    

