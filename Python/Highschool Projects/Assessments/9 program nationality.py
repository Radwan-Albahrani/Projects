iqama_id = ["1212312341" , "2457398246"]
non_saudis = []
saudis = []
y = 0
z = 6
while (y<6):
    iqama = input("Enter an iqama number " + str(z) + " times: ")
    if len(iqama) == 10 and iqama[0] != "3":
        print("Iqama added to the list")
        z = z-1
        y = y+1
        iqama_id.append(iqama)
    else:
        print("Make sure it is 10-digits, or it doesn't start with 1 or 2")
  
for x in iqama_id:
    if x[0] == "1":
        saudis.append(x)
    elif x[0] == "2":
        non_saudis.append(x)
while True:
    sns = input("Enter S or NS (S = saudi, NS = non-saudi): ")
    if sns == "s" or sns == "S":
        print("Saudies are: " + str(saudis))
        
    elif sns == "ns" or sns == "Ns" or sns == "nS" or sns == "NS":
        print("Non_saudis are: " + str(non_saudis))
        
    else:
        print("No Nationality found. Please retry.")


    
    
