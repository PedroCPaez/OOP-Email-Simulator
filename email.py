### --- OOP Email Simulator --- ###
"""
This program simulates an email inbox using object-oriented programming (OOP) principles.
It allows users to populate their inbox with sample emails, list the emails in their inbox,
read individual emails, view unread emails, and quit the application.

Classes:
    Email: Represents an email object with attributes such as email address, subject line,
           email content, and whether it has been read or not.

Functions:
    populate_inbox: Populates the inbox with sample email objects.
    list_emails: Lists the emails in the inbox.
    read_email: Displays the content of a selected email and marks it as read.
    main: The main function of the email program, providing a menu for users to interact with.
"""


# --- Email Class --- #
class Email:
    """Represents an email object.

        Attributes:
            has_been_read (bool): Indicates whether the email has been read or not.
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
    """

    # Declare the class variable, with default value, for emails.
    has_been_read = False

# Create the class, constructor and methods to create a new Email object.
    def __init__(self, email_address, subject_line, email_content):
        """Initializes an Email object with the given parameters.

        Args:
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
        """

    # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        """Marks the email as read by setting has_been_read to True."""

        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    """Populates the inbox with sample email objects."""

    global inbox
    # Create 3 sample emails and add it to the Inbox list.
    inbox.append(Email("sender1@example.com", "Welcome to HyperionDev!", "Welcome to our platform!"))
    inbox.append(Email("sender2@example.com", "Great job at the bootcamp!", "Keep up the good work!"))
    inbox.append(Email("sender3@example.com", "Your excellent grades!", "Congratulations on your achievements!"))


def list_emails():
    """Lists the emails in the inbox."""

    if inbox:
        print("\n\033[93mYour emails:\033[0m")
        for i, email in enumerate(inbox, start=1):
            print(f"{i}. {email.subject_line}")
    else:
        print("\n\033[91mInbox empty.\033[0m")


def read_email():
    # Create a function which displays a selected email.
    """Displays the content of a selected email and marks it as read."""

    list_emails()
    try:
        email_index = int(input("\n\033[93mEnter the email number you want to read: \033[0m"))
        email = inbox[email_index - 1]
        print(
            f"\nEmail_Id: \t{email_index}\n"
            f"Email from: \t{email.email_address}\n"
            f"Subject: \t{email.subject_line}\n"
            f"Content: \t{email.email_content}\n"
            )

        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        email.mark_as_read()
        print(f"\033[92mEmail_Id: {email_index}, Subject: {email.subject_line}, marked as read.\033[0m")
    except (ValueError, IndexError):
        print("\033[91mInvalid email number. Please try again.\033[0m")


# --- Email Program --- #
def main():
    """The main function of the email program."""


    # Call the function to populate the Inbox for further use in your program.
    populate_inbox()
    list_emails()

    user_choice = 0

    # Fill in the logic for the various menu operations.
    while user_choice != 3:
        user_choice = input('''\n\t\033[93mWould you like to:\033[0m
        1. Read an email
        2. View unread emails
        3. Quit application

        \033[93mPlease select an option: \033[0m''')

        if user_choice == '1':
            # add logic here to read an email
            read_email()

        elif user_choice == '2':
            # add logic here to view unread emails
            unread_emails = [email for email in inbox if not email.has_been_read]
            if unread_emails:
                print("\n\033[93mYour unread emails:\033[0m")
                for email in unread_emails:
                    index = inbox.index(email) + 1
                    print(f"{index}. {email.subject_line}")
            else:
                print("\n\033[91mYou have no unread emails.\033[0m")

        elif user_choice == '3':
            # add logic here to quit appplication
            print("\033[92mGoodbye!\033[0m")
            break

        else:
            print("\033[91mOops - incorrect option.\033[0m")


if __name__ == "__main__":
    main()
