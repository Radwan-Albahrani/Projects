iqama_list = ["1212312341" , "1457398246" , "7865269453"]

while True:
    iqama = input("Enter your 10-digit Iqama number: ")
    if iqama not in iqama_list and len(iqama) != 10:
        print("You are not in the system, or Invalid length")
    else:
        print("Welcome")
        break
