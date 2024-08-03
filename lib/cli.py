# lib/cli.py

from helpers import (
    exit_program,
    view_projects,
    add_project,
    selected_project,
    add_expense,
    update_project,
    view_project_expenses,
    delete_project
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
        print('\n**************************************************************\n')
        print(' Please select from the options below...\n\n project number: to view project details\n b: to go back\n a: to add a new project\n e: to exit')
        print('\n**************************************************************\n')
        choice = input('> ').lower()
        if choice == "b":
            break
        elif choice == "e":
            exit_program()
        elif choice == "a":
            add_project()
        else:
            try:
                project_id = int(choice)
                if Project.find_by_id(project_id):
                    selected_project(project_id)
                    project_menu(project_id)
                else:
                    print('Invalid project number entered')
            except ValueError:
                print('Invalid options')

def project_menu(project_id):
    while True:
        print('Would you like to...\n a: add an expense\n u: update project details\n v: view all project expenses\n d: delete project\n b: to go back\n e: to exit')
        print('\n**************************************************************\n')
        choice = input('> ')
        options = {
            "a": add_expense,
            "u": update_project,
            "v": view_project_expenses
        }
        if choice == "b":
            break
        elif choice == "e":
            exit_program()
        elif choice == "d":
            delete_project(project_id)
            view_projects_menu()
        elif choice in options:
            options[choice](project_id)
        else:
            print('Invalid option')


def menu():
    print('**************************************************************\n')
    print("Please select an option...")
    print("p: To view projects")
    print("e: To exit the program")


if __name__ == "__main__":
    main()
