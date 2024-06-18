# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

def command_parser():
    commands = ["help", "issue", "contact support"]
    user_input = input("Enter your command: ")

    for command in commands:
        if command in user_input:
            if command == "help":
                print("Here is the help information.")
            elif command == "issue":
                print("Please describe the issue you are facing.")
            elif command == "contact support":
                print("You can contact support at support@help.com.")
            break
command_parser()

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

def issue_categorizer():
    user_input = input("Enter the issue description: ")
    issue_keywords = ["login", "performance", "error", "bug", "crash"]

    for keyword in issue_keywords:
        if keyword in user_input:
            print(f"The issue category is: {keyword.capitalize()}")
            break
    else:
        print("Issue category not identified.")
        
issue_categorizer()

