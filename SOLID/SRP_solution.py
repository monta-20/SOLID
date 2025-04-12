class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserDB:
    def save_user(self, user):
        # Code to save user to database
        print(f"Saving {user.name} to database...")

class EmailService:
    def send_welcome_email(self, user):
        # Code to send welcome email
        print(f"Sending welcome email to {user.email}...")

# Usage
user = User("Montassar", "montassarbenbrahim29@gmail.com")
db = UserDB()
email_service = EmailService()

db.save_user(user)
email_service.send_welcome_email(user)

"""

Improvements:

    User class only handles user data

    UserDB class handles database operations

    EmailService class handles email sending

Each class now has a single responsibility, making the code:

    Easier to maintain

    Less prone to bugs

    More reusable

    Easier to test

"""