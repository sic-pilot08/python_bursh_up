responses = {}

polling_status = True

while polling_status:
    name = input("\nEnter you name: ")
    response = input("Which mountain would you like to climb today? ")
    responses[name] = response

    repeat = input("Would you like to let another person to respond? (yes/ no) ")

    if repeat == "no":
        polling_status = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
