pin = ("1234")

while True:
    pins = input("Enter the pin: ")
    if len(pins) != 4 or pins != pin:
        print("wrong pin. or invalid lengeth")
    else:
        print("welcome")
