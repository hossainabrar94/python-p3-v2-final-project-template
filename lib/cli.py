# lib/cli.py

from helpers import (
    exit_program,
    view_projects,
    add_project,
    selected_project,
    update_project,
    delete_project,
    add_expense,
    view_project_expenses,
    delete_project_expense,
    update_project_expense,
    selected_expense,
)
from models.project import Project
from models.expense import Expense


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


# ********************************************************************     Project Menues       ****************************************************************************
def view_projects_menu():
    project_id_map = view_projects()
    while True:
        print(' All Project Menu: Please select from the options below...\n\n project number: to view project details\n b: back to main menu\n a: to add a new project\n e: to exit')
        print('\n**************************************************************\n')
        choice = input('> ').lower()
        if choice == "b":
            main()
        elif choice == "e":
            exit_program()
        elif choice == "a":
            add_project()
            view_projects_menu()
        else:
            try:
                index = int(choice)
                project_id = project_id_map.get(index)
                if Project.find_by_id(project_id):
                    project_menu(project_id)
                else:
                    print('\n**************************************************************\n')
                    print('Invalid project number entered')
                    view_projects()
            except ValueError as e:
                print(f'Error: {e}')

def project_menu(project_id):
    selected_project(project_id)
    while True:
        print(' Project Menu: Would you like to...\n\n u: update project details\n v: view all project expenses\n d: delete project\n b: back to all projects\n e: to exit')
        print('\n**************************************************************\n')
        choice = input('> ')
        options = {
            "u": update_project,
            "v": view_project_expenses_menu
        }
        if choice == "b":
            view_projects_menu()
        elif choice == "e":
            exit_program()
        elif choice == "d":
            delete_project(project_id)
            view_projects_menu()
        elif choice in options:
            options[choice](project_id)
        else:
            print('Invalid option')


# ********************************************************************     Expense Menues       ****************************************************************************
def view_project_expenses_menu(project_id):
    print('\n**************************************************************\n')
    expense_id_map = view_project_expenses(project_id)
    while True:
        print(' All Project Expense Menu: Please select from the options below...\n\n expense number: to view expense detail\n a: to add an expense\n b: back to project menu\n e: to exit')
        print('\n**************************************************************\n')
        choice = input('> ')
        if choice == "b":
            project_menu(project_id)
        elif choice == "e":
            exit_program()
        elif choice == "a":
            add_expense(project_id)
            view_project_expenses_menu(project_id)
        else:
            try:
                index = int(choice)
                expense_id = expense_id_map.get(index)
                if Expense.find_by_id(expense_id):
                    expense_menu(expense_id, project_id)
                else:
                    print('\n**************************************************************\n')
                    print('Invalid expense number entered')
                    print('\n')
                    view_project_expenses(project_id)
            except ValueError as e:        
                print(f'Error: {e}')
        
def expense_menu(expense_id, project_id):
    selected_expense(expense_id)
    print('\n')
    while True:
        print(' Expense Menu: Would you like to...\n\n u: update expense details\n d: delete the expense\n b: back to all expenses\n e: to exit')
        choice = input('> ')
        if choice == "b":
            view_project_expenses_menu(project_id)
        elif choice == "e":
            exit_program()
        elif choice == "d":
            delete_project_expense(expense_id)
            view_project_expenses_menu(project_id)
        elif choice == "u":
            update_project_expense(expense_id)
        else:
            print('Invalid option')


# ********************************************************************     Main Menues       ****************************************************************************
def menu():
    print('**************************************************************\n')
    print(" Main Menu: Please select an option...")
    print(" p: To view projects")
    print(" e: To exit the program")


if __name__ == "__main__":
    main()