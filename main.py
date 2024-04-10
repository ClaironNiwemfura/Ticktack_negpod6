def create_event():
    print("\nCreating an event...")

def update_event():
    print("\nUpdating an event...")

def delete_event():
    print("\nDeleting an event...")

def set_priority_event():
    print("\nSetting priority for an event...")


def see_statistics():
    print("\nViewing statistics...")
    
def start_timer():
    print("\nStarting a timer...")
    
def stop_timer():
    print("\nStopping a timer...")
    
def see_open_timers():
    print("\nViewing open timers...")

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
            timer_menu()
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

    
def timer_menu():
    while True:
        print("\nTimer Menu:")
        print("----------")
        print("1. Start a timer")
        print("2. Stop a timer")
        print("3. See the Open Timers")
        print("4. Back to Main Menu")
       

        choice = input("Enter your choice: ")

        if choice == '1':
            start_timer()
        elif choice == '2':
            stop_timer()
        elif choice == '3':
            see_open_timers()     
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
