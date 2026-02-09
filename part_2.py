#3
rover_status = {
    "Battery" : 100,
    "Heater" : "Off",
    "Camera" : "Standby"
}

mission_log = [
    {
        "Site": "Crater A", 
        "Radiation": "Low", 
        "Water": False
    },
    {
        "Site": "Dune B", 
        "Radiation": "High", 
        "Water": True
    }
]

for site in mission_log:
    print(f"Site {site['Site']} has {site['Radiation']} radiation.")

print(rover_status["Battery"])

rover_status["Battery"] = 85
rover_status["Heater"] = "On"
rover_status["Speed"] = 5

print(rover_status)


