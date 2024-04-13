
import sqlite3

def set_event_priority(event_id, is_priority):
    """Sets the priority flag for an event in the events table.

    Args:
        event_id (int): The unique identifier of the event.
        is_priority (bool): True to set priority, False to remove priority.
    """

    connection = None
    cursor = None
    try:
        connection = sqlite3.connect('ticktack.db')
        cursor = connection.cursor()

        priority_value = 1 if is_priority else 0
        cursor.execute("UPDATE events SET priority=? WHERE event_id=?", (priority_value, event_id,))
        connection.commit()
        print("Event priority updated successfully!")
    except sqlite3.Error as e:
        print("Error setting event priority:", e)
        if connection:
            connection.rollback()  # Rollback if an error occurs
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
