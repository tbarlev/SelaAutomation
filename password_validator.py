# This script validates a given password

#Import color library to print output in color
import colorama
from colorama import Fore
import sys

def validate(passwd):
    """
    Validate password - length, charachters
    :param passwd:
    :return: 0 if password is valid, 1 if not valid + reason
    """
    global reason

    if len(passwd) < 10:
        print(len(passwd))
        reason = "Password should be at least 10 charachters"
        return 1

    if not any(char.isdigit() for char in passwd):
        reason = "Password should have at least one numeric charachter"
        return 1

    if not any(char.isupper() for char in passwd):
        reason = "Password should have at least one uppercase letter"
        return 1

    if not any(char.islower() for char in passwd):
        reason = "Password should have at least one lowercase letter"
        return 1

    return 0

# validate input arguments
if len(sys.argv) == 3:
    if sys.argv[1] == "-f":
        fl = open(sys.argv[2], "r")
        passwd = fl.read()
else:
    if len(sys.argv) == 2:
            passwd = sys.argv[1]

    else:
        print("Incorrect arguments")
        exit()

# passwd = sys.argv[1]

if validate(passwd):
        print(Fore.RED + "password is not valid, " + reason)
else:
        print(Fore.GREEN + "Password is valid")












