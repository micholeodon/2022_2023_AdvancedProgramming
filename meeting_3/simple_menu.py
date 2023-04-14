
# Initialize a variable to store the user's choice
choice = 0

# Keep looping until the user chooses to exit
while choice != 4:
    # Display the menu
    print("==== MENU ====")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")    
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    
    # Check the user's choice and execute the corresponding code
    if choice == 1:
        print("Option 1 selected")
    elif choice == 2:
        print("Option 2 selected")
    elif choice == 3:
        print("Option 3 selected")
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice, please try again")
