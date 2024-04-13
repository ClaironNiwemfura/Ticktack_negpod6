import sqlite3
from datetime import datetime 


# Example use of dbConfig connection
# from dbConfig import conn
# cursor = conn.cursor() 
# # statements eg cursor.execute("SELECT * FROM events")
# conn.commit()
# cursor.close()
# conn.close()


# Global variables
event_name = ''
start_date = ''
end_date = ''
description=''

start_time = None

# Function to create event
#-------------------------
def create_event():
    """Create a new event."""
    global event_name, start_date, end_date, description
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
        return end_date
    # Preview the event details
    print('\nEvent Details:')
    print(f'Name: {event_name}')
    print(f'Start Date: {sdatetime.date()}')
    print(f'End Date: {edatetime.date()}')
    print(f"Description: \n{description}")

    confirmation = input("\nIs this information correct? y/n\n").lower()
    while confirmation not in ['y', 'yes']:
        if confirmation == 'n':
            return create_event()
        else:
            break

    print("\nEvent created successfully!")
    
    # Missing database to store the event information

# Function to Update event
#-------------------------
def update_event():
    """Update an existing event."""
    global event_name, start_date, end_date, description
    #List the existing  events for user to select one to update
    pass
    #After chosing the event to update, you will start to update the event 
    event_name = input('Enter updated event name: ')
    start_date = input('Enter updated the starting date (YYYY-MM-DD): ')
    end_date = input('Enter updated the ending date (YYYY-MM-DD): ')
    description = input('Enter updated brief description of the event:\n')


 # Function to list available timer from database
    #--------------------------------------------
def list_timers():
    # Connect to the database. Assume the database named is 'timers.db'

    conn = sqlite3.connect('timers.db')
    cursor = conn.cursor()

    # Fetch all timers sorted by start_date
    cursor.execute("SELECT start_date, end_date FROM timers ORDER BY start_date")
    timers = cursor.fetchall()

    # Check if there are timers
    if len(timers) == 0:
        print("No timers stored in the database.")
    else:
        print("List of Timers:")
        for timer in timers:
            start_date = datetime.strptime(timer[0], "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strptime(timer[1], "%Y-%m-%d %H:%M:%S")
            print(f"Start Date: {start_date}, End Date: {end_date}")

    # Close the database connection
    conn.close()

def delete_event():
    print("\nDeleting an event...")

def set_priority_event():
    print("\nSetting priority for an event...")


def see_statistics():
    print("\nViewing statistics...")
 
 
 
 # Function to start timer
#-------------------------  
def start_timer():
    global start_time
    start_time = datetime.now()
    print("\nTimer started at:", start_time)


# Function to stop timer
#-------------------------
def stop_timer():
    global start_time
    if start_time:
        end_time = datetime.now()
        print("Timer stopped at:", end_time)
        elapsed_time = end_time - start_time
        total_seconds = elapsed_time.total_seconds()
        hours = total_seconds // 3600
        print("Elapsed time:", hours, "hours")

         # Display message based on elapsed hours
        if hours > 4:
            print("Impressive feat")
        elif hours == 4:
            print("That's great")
        elif 2 <= hours <= 4:
            print("You sure you don't want to go for another round?")
        elif hours < 2:
            print("Hope you finished")

        start_time = None
    else:
        print("\nTimer hasn't been started yet.")

    
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
