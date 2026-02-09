#4.1
def sensor():
    travel_log = []
    while True:
        try:
            angle = int(input("Please enter sensor reading (Slope Angle): "))
        except ValueError:
            print("Sensor Glitch")
            continue
        else:
            if angle > 45:
                print("CRITICAL TILT! HALTING.")
                break
            else:
                travel_log.append(angle)
                print("Path Stable. Moving Forward")
                continue

sensor()