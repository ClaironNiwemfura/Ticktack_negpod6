import sqlite3
from datetime import datetime, timedelta
import re

# Example use of dbConfig connection
# from dbConfig import conn

from dbConfig import conn, cur 

# Example use of dbConfig connection
# from dbConfig import conn
cur = conn.cursor() 
# # statements eg cursor.execute("SELECT * FROM events")
# conn.commit()

# Global variables
event_name = ''
start_time = ''
end_time = ''
description=''

timer_id = None
start_time = None


 # Function to list available timer from database
#--------------------------------------------
def list_timers():
    # Connect to the database. Assume the database named is 'timers.db'

    conn = sqlite3.connect('timers.db')
    cursor = conn.cursor()
    
    # Fetch all timers sorted by start_time
    cursor.execute("SELECT start_time, end_time FROM timers ORDER BY start_time")
    timers = cursor.fetchall()

    # Check if there are timers
    if len(timers) == 0:
        print("No timers stored in the database.")
    else:
        print("List of Timers:")
        for timer in timers:
            start_time = datetime.strptime(timer[0], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(timer[1], "%Y-%m-%d %H:%M:%S")
            print(f"Start Date: {start_time}, End Date: {end_time}")

    # Close the database connection
    conn.close()
# Function to create event
#-------------------------
def create_event():
    cursor = conn.cursor()
    """Create a new event."""
    dateFormat = r'^20\d{2} (0[1-9]|1[0-2]) (0[1-9]|[12]\d|3[01]) (2[0-3]|[01]\d)\:[0-5]\d'

    event_name = input('Enter event name: ')
    description = input('Enter a brief description of the event:\n')
    while True:
        start_time = input('Enter the starting date (YY MM DD HH:MI): ')
        if re.match(dateFormat, start_time):
            break
        else:
             print("Incorrect time format! Please check the format and try again.",dateFormat,start_time)
    while True:
        end_time = input('Enter the Ending date (YY MM DD HH:MI): ')
        numstart = int(start_time.replace(" ","").replace(":",""))
        numend = int(end_time.replace(" ","").replace(":",""))
        if re.match(dateFormat, end_time)  and numstart < numend:
            break
        else:
            print("Start time should be less than end time. Please check the format and try again.")
    try:
        print('\nEvent Details:')
        print(f'Name: {event_name}')
        print(f"Description: \n{description}")
        print(f'Start Time: {start_time}')
        print(f'End Time: {end_time}')
        confirmation = input("\nIs this information correct? y/n\n").lower()
        if confirmation == 'n':
            return create_event()
        else:
            sql = "INSERT INTO events(name, description,from_time, to_time) VALUES('"+event_name+"','"+description+"','"+start_time+"','"+end_time+"')"  
            print("query: ",sql)
            print("\nEvent created successfully!")
            cursor.execute(sql)
            conn.commit()
            
        
        
    except Exception as e:
        print("There was an error: ",e," try again")
        return event_menu()
    cursor.close()


# Function to Update event
#-------------------------
def update_event():
    cursor = conn.cursor()
    try:
        """Update an existing event."""
        ev_id = input("Enter the id of event you want to change: ")
        sql = "SELECT * FROM events WHERE id ="+ev_id
        cursor.execute(sql) 
        if not cursor.fetchone():
            print("Event with id", ev_id," not found. Refer to the list of events!")
            return event_menu()
        dateFormat = r'^20\d{2} (0[1-9]|1[0-2]) (0[1-9]|[12]\d|3[01]) (2[0-3]|[01]\d)\:[0-5]\d'

        event_name = input('Enter event name: ')
        description = input('Enter a brief description of the event:\n')
        while True:
            start_time = input('Enter the starting date (YY MM DD HH:MI): ')
            if re.match(dateFormat, start_time):
                break
            else:
                 print("Incorrect time format! Please check the format and try again.",dateFormat,start_time)
        while True:
            end_time = input('Enter the Ending date (YY MM DD HH:MI): ')
            numstart = int(start_time.replace(" ","").replace(":",""))
            numend = int(end_time.replace(" ","").replace(":",""))
            if re.match(dateFormat, end_time)  and numstart < numend:
                break
            else:
                print("Start time should be less than end time. Please check the format and try again.")

        
        print('\nEvent Details:')
        print(f'Name: {event_name}')
        print(f"Description: \n{description}")
        print(f'Start Time: {start_time}')
        print(f'End Time: {end_time}')
        confirmation = input("\nIs this information correct? y/n\n").lower()
        if confirmation == 'n':
            return update_event()
        else:
            sql = "UPDATE events SET name = '"+event_name+"', description='"+description+"',from_time = '"+start_time+"', to_time = '"+end_time+"' WHERE id = "+ev_id  
            print("query: ",sql)
            print("\nEvent Updated Successfully!")
            cursor.execute(sql)
            conn.commit()
            
        
        
    except Exception as e:
        print("There was an error: ",e," try again")
        return event_menu()
    cursor.close()
# Function to delete event
def delete_event():
    cursor = conn.cursor()
    try:
        """Delete an existing event."""
        ev_id = input("Enter the id of event you want to delete: ")
        sql = "SELECT * FROM events WHERE id ="+ev_id
        cursor.execute(sql)
        record = cursor.fetchone()
        if not record:
            print("Event with id", ev_id," not found. Refer to the list of events!")
            return event_menu()
        print("\n\n| {:<10} | {:<20} | {:<15} | {:<10} | {:<10} |".format("Event ID", "Event Name","Event Description", "Event Start Time", "Event End Time"))
        print("-" * 98)
        print("| {:<10} | {:<10} | {:<15} | {:<10} | {:<10} |".format(record[0], record[1], record[2], record[3].strftime("%Y-%m-%d %H:%M"),record[4].strftime("%Y-%m-%d %H:%M")))
        confirmation = input("Is this the record you want to delete?y/n\n").lower()

        if confirmation == 'n':
            return delete_event()
        else:
            sql = "DELETE FROM events WHERE id = "+ev_id  
            print("query: ",sql)
            print("\nEvent removed Successfully!")
            cursor.execute(sql)
            conn.commit()
            
        
        
    except Exception as e:
        print("There was an error: ",e," try again")
        return event_menu()
    cursor.close()


def view_all_events():
    """Viewing all events"""
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM events"
        print("query: ",sql)
        cursor.execute(sql)
        event_list = cursor.fetchall()
        print("Event list: ",event_list,"\n\n")
        # Print table header
        print("| {:<10} | {:<20} | {:<15} | {:<10} | {:<10} |".format("Event ID", "Event Name","Event Description", "Event Start Time", "Event End Time"))
        print("-" * 98)

        # Print rows in a table format
        for row in event_list:
            # print(row[3].strftime("%Y-%m-%d %H:%M"))
            print("| {:<10} | {:<10} | {:<15} | {:<10} | {:<10} |".format(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d %H:%M"),row[4].strftime("%Y-%m-%d %H:%M")))
        conn.commit()               
    except Exception as e:
        print("There was an error: ",e," try again")
        return view_all_events()
    cursor.close()

def see_statistics():
    print("\n...Your Statistics...")

    # Query to fetch all records from the 'timers' table
    cur.execute("SELECT from_time, to_time FROM timers")

    # Fetch all rows from the query
    timers = cur.fetchall()

    # Calculate the total elapsed time for all timers
    total_elapsed_time = timedelta()  # Start with a timedelta of zero

    # Iterate through all timers and calculate elapsed time
    for from_time, to_time in timers:
        if to_time is None:  # If the timer has not been stopped yet, ignore it
            continue

        # Calculate elapsed time for each timer
        elapsed_time = to_time - from_time
        total_elapsed_time += elapsed_time

    # Convert the total elapsed time to total hours
    total_hours = total_elapsed_time.total_seconds() / 3600  # Convert seconds to hours

    # Print total elapsed time in a readable format
    print(f"Total elapsed time: {total_hours:.2f} hours")

    # Determine productivity based on total elapsed time
    if total_hours > 5:
        print("You have been very productive today!")
    elif total_hours < 1:
        print("You need to work harder today.")
    else:
        print("You have had moderate performance today.")
 
 # Function to start timer
#-------------------------  

def start_timer():
    global timer_id
    global start_time

    # Get the current time as the start time
    start_time = datetime.now()
    print("\nTimer started at:", start_time)

    # Insert the start time into the 'timers' table
    cur.execute(
        "INSERT INTO timers (from_time) VALUES (%s) RETURNING id",
        (start_time,)
    )

    # Retrieve the generated ID (timer ID)
    timer_id = cur.fetchone()[0]

    # Commit the transaction to the database
    conn.commit()

def stop_timer():
    global timer_id
    global start_time

    # Check if a timer was started
    if timer_id is None:
        print("Timer hasn't been started yet.")
        return

    # Get the current time as the end time
    end_time = datetime.now()
    print("\nTimer stopped at:", end_time)

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time)

    # Update the 'timers' table with the end time
    cur.execute(
        "UPDATE timers SET to_time = %s WHERE id = %s",
        (end_time, timer_id)
    )

    # Commit the transaction to the database
    conn.commit()

    # Reset the timer ID and start time
    timer_id = None
    start_time = None
    
def timer_history():
    print("\nViewing timer history...")
    
    # Query to fetch all records from the 'timers' table
    cur.execute("SELECT * FROM timers")
    
    # Fetch all rows from the query
    timers = cur.fetchall()
    
    # Print the header
    print("ID | Start Time | End Time")
    print("-" * 30)
    
    # Iterate through all timers and print each one
    for timer in timers:
        id, from_time, to_time = timer
        print(f"{id} | {from_time} | {to_time}")
        
    
    

def main_menu():
    while True:
        print("\nMain Menu:")
        print("-------------")
        print("1. Create and Manage an event")
        print("2. Manage your timer")
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
            conn.close()
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
        print("4. See all events")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_event()
        elif choice == '2':
            update_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            view_all_events()
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
        print("3. timer history")
        print("4. Back to Main Menu")
       

        choice = input("Enter your choice: ")

        if choice == '1':
            start_timer()
        elif choice == '2':
            stop_timer()
        elif choice == '3':
            timer_history()     
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
    
