birds1 = ["Crow","Blackbirds","Doves","Ducks","Chickens"]
birds2 = ["Gulls","Finches","Flycatchers","Herons","Kingfishers"]
birds1.extend(birds2)
birds1.append("Red rail")
birds = input("Enter a name of a bird: ")

if birds in birds1:
    print(birds + " is in the list")
else:
    print(birds + "is not in the list")
