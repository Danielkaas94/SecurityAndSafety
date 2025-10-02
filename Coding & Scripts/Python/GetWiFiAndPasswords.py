
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

    5th January 2024
"""


from colorama import Fore, Back, Style

import subprocess

"""
Anytime you're playing music for the crowd
Instead of yourself
You're fucked
"""


def get_wifi_passwords(profiles):
    """
    This is based on the terminal command:

    netsh wlan show profile name="Name" key=clear

    :param profiles: A list of all the known WiFi connections
    :return: print text with SSID || Password
    """

    # Get Passwords
    for profile in profiles:

        try:
            # Run the netsh command to retrieve Wi-Fi profile names
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile', f'name={profile}', 'key=clear'], capture_output=True, text=True, check=True)

            # You have to look for "Key Content            : "
            """
            Security settings 
            ----------------- 
                Authentication         : WPA2-Personal
                Cipher                 : CCMP
                Authentication         : WPA2-Personal
                Cipher                 : GCMP
                Security key           : Present
                Key Content            : !#!¤#%¤&#%
            """

            # Extract Wi-Fi profile names from the output

            # Find the position of "Key Content"
            key_content_start = result.stdout.find("Key Content")

            # Extract the value after "Key Content"
            key_content_substring = result.stdout[key_content_start + len("Key Content"):]

            # Find the end position of the line containing "Key Content"
            key_content_end = key_content_substring.find('\n')

            # Extract the value without considering the lines after "Key Content"
            key_content_value = key_content_substring[:key_content_end].strip()

            print(Fore.BLUE + f"SSID: {profile}  || Password: {key_content_value}")

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")




def get_wifi_profiles():
    """
    This is based on the terminal command:

    netsh wlan show profiles

    :return:
    """

    # Get SSID
    print("Get WiFi names!")

    try:
        # Run the netsh command to retrieve Wi-Fi profile names
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)

        # print(f"Result: {result}")

        # Extract Wi-Fi profile names from the output
        profiles = [line.split(":")[1].strip() for line in result.stdout.splitlines() if "All User Profile" in line]

        # print(f"Profiles: {profiles}")

        # Print the list of Wi-Fi profiles
        print("Wi-Fi Profiles:")
        for profile in profiles:
            print(Fore.CYAN + profile)

        get_wifi_passwords(profiles)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
