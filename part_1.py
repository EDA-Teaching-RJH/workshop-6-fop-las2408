#1.4
sample_bay = [ "Basalt", "Silica", "Iron", "Dust" ]
new_findings = []

#print(sample_bay[0])
#print(sample_bay[-1])
#print(len(sample_bay))

#for sample in sample_bay:
    #print(f"Transmitting data for: {sample}")

#i = 0
#while i < 3:
    #rock = str(input("Please input the rock type: "))
    #new_findings.append(rock)
    #i = i + 1
    #continue
#else:
    #print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    print(sample_bay)
else:
    print(sample_bay)