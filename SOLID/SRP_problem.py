class User : 
    def __init__(self, name , email):
        self.name = name 
        self.email = email 
    def save_to_database(self) : 
        print(f"Saving {self.name} to database ...")
    def send_welcome_email(self) : 
        print(f"Sending welcome email to {self.email}... ")

user = User("Montassar"  , "montassarbenbrahim29@gmail.com")
user.save_to_database()
user.send_welcome_email()

"""
Problem: This User class has multiple responsibilities:

    Managing user data

    Database operations

    Email sending

"""