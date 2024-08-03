# lib/cli.py

from helpers import (
    exit_program,
    view_projects,
    add_project,
    selected_project,
    add_expense,
    update_project
)
from models.project import Project


def main():
    while True:
        menu()
        choice = input("> ").lower()
        options = {
            "e" : exit_program,
            "p" : view_projects_menu
        }
        if choice in options:
            options[choice]()
        else:
            print('Invalid option')

def view_projects_menu():
    view_projects()
    while True:
        print('Select a project by number to view details\n or\n b: to go back\n or\n a: to add a new project\n or\n e: to exit')
        choice = input('> ').lower()
        if choice == "b":
            break
        elif choice == "e":
            exit_program()
        elif choice == "a":
            add_project()
        try:
            project_id = int(choice)
            if Project.find_by_id(project_id):
                selected_project(project_id)
                project_menu(project_id)
            else:
                print('Invalid project number entered')
        except ValueError:
            print('Invalid option')

def project_menu(project_id):
    while True:
        print('a: add an expense\n u: update project details\n b: to go back\n e: to exit')
        choice = input('> ')
        options = {
            "a": add_expense,
            "u": update_project,
            "e": exit_program
        }
        if choice == "b":
            break
        elif choice in options:
            options[choice](project_id)
        else:
            print('Invalid option')


def menu():
    print("Please select an option:")
    print("p: To view projects")
    print("e: To exit the program")


if __name__ == "__main__":
    main()
