#3.1
while True:
        try:
               motor_speed = int(input("Enter Motor Speed: "))
        except ValueError:
            print("Error: Corrupted Signal. Maintaining current speed.")
            continue
        
        else:
              print(f"Speed set to {motor_speed}")
              break

            
    

