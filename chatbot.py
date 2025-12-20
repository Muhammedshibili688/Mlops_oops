class Chatbot:
    users = {}
    def __init__(self, name = "Travis Doe", 
                 password = "", loggedin = False):
        
        self.name = name
        self.password = password
        self.loggedin = loggedin

    def menu(self):
        print(
            "Welcome to the Chatbot System"
            "\n1. Register"
            "\n2. Login"
            "\n3. Chat"
            "\n4. Exit"
            )
        choice = input("Please enter your choice (1-4): ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.chat
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


    def register(self):
        print("Register a new account")
        name = input ("Enter your name: ")
        password = input("Enter your password: ")
        self.users[name] = password
        print("Registration Succesful!")

    def login(self):
        print("Login to your account")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name in self.users and self.users[name] == password:
            self.loggedin = True
            print("Login Successful!\n Welcome, " +name+"!")
            return True
        else:
            print("Login Failed! Please check your credentials.")
            return False
        
    
    def chat(self):
        if not self.loggedin:
            print("You must be loggedin first.")
            return

        print("You are now chatting with the bot. Type 'exit' to logout.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                self.loggedin = False
                print("You have logged out.")
                break
            else:
                print("Bot: I'm here to help you!")
    def exit(self):
        print("Exiting the system. Goodbye!")
        
if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        chatbot.menu()
        if chatbot.loggedin:
            chatbot.chat()