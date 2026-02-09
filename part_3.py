#3.3

def get_coordinate():
    while True:
        try:
            coord = int(input("Please enter an x coordinate: "))

        except ValueError:
            print("Invalid coordinate")
            continue
        else:
            if coord > 100 or coord < -100:
                print("Coordinate out of range")

            else:
                print(f"Coordinate is {coord} - within accepted range")
                break
    
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

            
    

