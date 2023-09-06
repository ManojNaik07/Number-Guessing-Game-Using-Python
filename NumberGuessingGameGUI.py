import tkinter as tk
from tkinter import messagebox
from backend import NumberGuessingGame
from NumberGuessingGameUI import NumberGuessingGameUI
import os

class NumberGuessingGameGUI:
    def __init__(self):
        self.game = NumberGuessingGame()

        self.window = tk.Tk()
        self.window.title("Number Guessing Game")

        self.username_label = tk.Label(self.window, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.window, text="Register", command=self.show_registration)
        self.register_button.pack()

        self.registration_window = None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform validation
        if self.validate_credentials(username, password):
            self.start_game()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def validate_credentials(self, username, password):
        '''if not os.path.isfile("credentials.txt"):
            with open("credentials.txt", "w") as file:
                pass  # Create an empty file if it doesn't exist'''
        if os.stat("D:\credentials.txt").st_size==0:
            print("File")
            return False

        with open("D:\credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
        return False

    def show_registration(self):
        if self.registration_window is not None:
            self.registration_window.destroy()

        self.registration_window = tk.Toplevel(self.window)
        self.registration_window.title("Registration")

        self.reg_username_label = tk.Label(self.registration_window, text="Username:")
        self.reg_username_label.pack()

        self.reg_username_entry = tk.Entry(self.registration_window)
        self.reg_username_entry.pack()

        self.reg_password_label = tk.Label(self.registration_window, text="Password:")
        self.reg_password_label.pack()

        self.reg_password_entry = tk.Entry(self.registration_window, show="*")
        self.reg_password_entry.pack()

        self.register_button = tk.Button(self.registration_window, text="Register", command=self.register)
        self.register_button.pack()

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        # Perform registration
        if self.validate_credentials(username, password):
            messagebox.showwarning("Registration Failed", "Username already exists!")
        else:
            with open("D:\credentials.txt", "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Registration Successful", "You have been registered successfully!")
            self.registration_window.destroy()

    def start_game(self):
    # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate the username
        if not self.validate_username(username):
            messagebox.showerror("Invalid Username", "Please enter a valid username!")
            return

        # Validate the credentials and start the game
        if self.validate_credentials(username, password):
            self.window.destroy()  # Close the login window

            # Execute the file containing the game UI
            #os.system("python NumberGuessingGameUI.py")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def validate_username(self, username):
        # Perform any necessary validation for the username
        if not username or len(username.strip()) == 0:
            return False
        return True

# Create an instance of the GUI and run it
login_gui = NumberGuessingGameGUI()
login_gui.window.mainloop()

# Only start the game UI if the login was successful
if login_gui.start_game:
    game_ui = NumberGuessingGameUI()
    game_ui.run()
