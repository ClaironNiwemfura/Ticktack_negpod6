import sqlite3

def delete_event(event_id):
    """Deletes an event from the events table based on its ID.

    Args:
        event_id (int): The unique identifier of the event to be deleted.
    """

    connection = None
    cursor = None
    try:
        connection = sqlite3.connect('ticktack.db')
        cursor = connection.cursor()

        cursor.execute("DELETE FROM events WHERE event_id=?", (event_id,))
        connection.commit()
        print("Event deleted successfully!")
    except sqlite3.Error as e:
        print("Error deleting event:", e)
        if connection:
            connection.rollback()  # Rollback if an error occurs
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
