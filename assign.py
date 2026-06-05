import time

def populate_list(list_name):
    """Helper function to populate a list until the user types 'yes'."""
    print(f"\n--- Populating {list_name} ---")
    user_list = []
    
    while True:
        # Prompt for the list item
        item = input(f"Enter an item for {list_name}: ")
        user_list.append(item)
        
        # Inner loop to safely catch the yes/no answer
        while True:
            is_through = input("Are you through? (yes/no): ").strip().lower()
            
            # Check if the input is strictly valid
            if is_through == 'yes' or is_through == 'no':
                break # Breaks this tiny safety loop to move on
            else:
                print("Invalid input. Please type exactly 'yes' or 'no'.")
                
        # If they finally said yes, break the main populating loop
        if is_through == 'yes':
            break
            
    return user_list

# 1 & 2. Populate list1 and list2
list1 = populate_list("List 1")
list2 = populate_list("List 2")

# 3. Check if lengths match
if len(list1) != len(list2):
    # It prints the message and gracefully reaches the end of the script (no error thrown)
    print("\nlength of lists don't match")
    
else:
    # 4. If lengths DO match, run the rest of the program
    print("\nlengths match. Proceeding", end="", flush=True)

    # Loop 3 times to print a period, waiting 1 second each time
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    print() # Moves to a new line after the periods

    # 5. Create a dictionary (list1 = Keys, list2 = Values)
    final_dictionary = dict(zip(list1, list2))

    print("\nFinal Dictionary:")
    print(final_dictionary)