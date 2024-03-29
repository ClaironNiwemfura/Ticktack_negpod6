def create_event():
    """Create a new event."""
    event_name = input('Enter event name: ')
    start_date = input('Enter the starting date (YYYY-MM-DD): ')
    end_date = input('Enter the ending date (YYYY-MM-DD): ')
    description = input('Enter a brief description of the event:\n')

    # Check if dates are valid and in correct format.
    try:
        from datetime import datetime
        sdatetime = datetime.strptime(start_date, '%Y-%m-%d')
        edatetime = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, please use YYYY-MM-DD")
        return create_event()

    if sdatetime > edatetime:
        print("The start date must be before the end date.")
        return create_event()
    print("\nEvent created successfully!")
    
    # Missing database to store the event information

def update_event():
    print("Updating an event...")

def delete_event():
    print("Deleting an event...")

def set_priority_event():
    print("Setting priority for an event...")

def start_timer():
    print("Starting a timer...")

def see_statistics():
    print("Viewing statistics...")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("-------------")
        print("1. Create and Manage an event")
        print("2. Start a timer")
        print("3. See your statistics")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            event_menu()
        elif choice == '2':
            start_timer()
        elif choice == '3':
            see_statistics()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def event_menu():
    while True:
        print("\nEvent Menu:")
        print("----------")
        print("1. Create an event")
        print("2. Update an event")
        print("3. Delete an event")
        print("4. Set priority for an event")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_event()
        elif choice == '2':
            update_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            set_priority_event()
        elif choice == '5':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
