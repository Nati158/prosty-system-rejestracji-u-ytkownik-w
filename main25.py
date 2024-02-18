class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_logged_in = False

    def login(self, entered_password):
        if entered_password == self.password:
            self.is_logged_in = True
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")

    def logout(self):
        self.is_logged_in = False
        print("Logged out successfully.")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

if __name__ == "__main__":
    user1 = User("john_doe", "john@example.com", "password123")
    print("User:", user1.username)
    print("E
