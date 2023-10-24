# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
from colorama import init, Fore, Style

def calculate_md5_hash(input_str):
    md5 = hashlib.md5()
    md5.update(input_str.encode('utf-8'))
    return md5.hexdigest()


def print_hi(name):
    """
    You just print the name on the console ✨💚
    :param name: Name to print
    :return: returns nothing
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Just Testing - BruteForce Get HashValue
def BruteForceGuessMD5_test2():

    MD5Hash = "973cc08c6aa6d171ed0ebf31675517ae"
    block1 = "ymca"
    block3 = "mmdk"

    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                for c4 in characters:
                    combination = f"{block1}{c1}{c2}{c3}{c4}{block3}"
                    # print(combination)

                    hash_value = calculate_md5_hash(combination)

                    #print(f"Input String: {combination}")
                    #print(f"MD5 Hash: {hash_value}")

                    if hash_value == MD5Hash:
                        print(Fore.CYAN + "You got it!!!")
                        print(f"Input String: {combination}")
                        print(f"MD5 Hash: {hash_value}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(__name__)
    print(0.1 + 0.2)  # DO YOU EVEN MATH?? 0.1 + 0.2 = 0.30000000000000004??

    green_text = "\033[32m"

    print_hi(green_text + 'Daniel Kaas Bundgaard Jørgensen')

    BruteForceGuessMD5_test2()