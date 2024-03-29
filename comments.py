# Define a dictionary to store menu options and messages
menu_options = {
    2: "Start working.",
    3: "Checkout your progress for the past few days.",
}

# Function to display a message based on user choice
def display_message(choice):
  """
  This function displays the message corresponding to the user's menu choice.

  Args:
      choice (int): The user's chosen menu option.
  """
  if choice in menu_options:
    print(menu_options[choice])
  else:
    print("Invalid option. Please choose a valid number from the menu.")
# Example usage (optional, for testing purposes)
if __name__ == "__main__":
  user_choice = int(input("Enter your choice (2,3): "))
  display_message(user_choice)
