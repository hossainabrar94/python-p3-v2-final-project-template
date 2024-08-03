# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "e" or "E":
            exit_program()
        elif choice == "P" or "p":
            helper_1()
        else:
            print("Invalid option")


def menu():
    print("Please select an option:")
    print("E/e: To exit the program")
    print("P/p: To view projects")


if __name__ == "__main__":
    main()
