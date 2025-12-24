class Chatbot:

    __user_id = 1

    def __init__(self, name = "", email = "",
                 password = "", loggedin = False):
        
        self.id = Chatbot.__user_id
        Chatbot.__user_id += 1
        self.name = name
        self.email = email
        self.password = password
        self.loggedin = loggedin

    def menu(self):

        print("""Welcome to the Chatbot System
            \n1. Register
            \n2. Login
            \n3. Chat
            \n4. Exit
            \n->"""
            )
        choice = input("Please enter your choice (1-4): ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.chat()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

    @staticmethod       
    def get_id():
        return Chatbot.__user_id
    
    @staticmethod
    def set_id(val):
        Chatbot.__user_id = val

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def register(self):

        print("Register a new account")
        self.name = input("Enter your name: ")
        self.email = input ("Enter your email: ")
        self.password = input("Enter your password: ")
        print("Registration Successful !!")

        print("\n")
        self.menu()

    def login(self):

        print("Login to your account")
        email_uname = input("Enter your email/username: ")
        pwd = input("Enter your password: ")

        if email_uname == '' and pwd == '':
            print("Please signup first by pressing 1 in the main menu")
        
        else:
            if  (email_uname == self.email or email_uname == self.name) and self.password == pwd:
                self.loggedin = True
                print("Login Successful!\nWelcome, " +self.name+" !!")
                chat_opt = input("\nTo use Chatbot, Type 'chat': ")

                if chat_opt.strip().lower() == 'chat':
                    self.chat()
                else:
                    print("\nSpelling miskate in input...")
            
            else:
                print("Login Failed! Please Enter your correct credentials.")
                return False
        
        print("\n")
        self.menu()
        
    
    def chat(self):

        if self.loggedin is False:
            print("You must be loggedin first.")
            return self.menu()

        print("You are now chatting with the bot. Type 'exit' to logout.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                self.loggedin = False
                print("You have logged out.")
                break

            else:
                print("Bot: I'm here to help you!")
                print("\n")
        
        print("\n")
        self.menu()
                

    def exit(self):
        print("Exiting the system. Goodbye!")
        exit()

'''       
if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        chatbot.menu()
        if chatbot.loggedin:
            chatbot.chat()
'''