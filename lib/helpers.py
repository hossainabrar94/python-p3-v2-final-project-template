# lib/helpers.py
from models.expense import Expense
from models.project import Project

def view_projects():
    print('\n**************************************************************\n')
    print("Projects:")
    projects = Project.get_all()
    for project in projects:
        print(f'{project.id}. {project.name}')
    
def add_project():
    while True:
        print('**************************************************************\n')
        name = input("Please enter project's name: ")
        if not name or name.isdigit():
            print('Please enter a valid name that contains alphabetic characters')
            continue
        quote = input("Please enter project's quote: ")
        try:
            quote = float(quote)
        except ValueError:
            print('Please enter a valid number')
            continue
        try:    
            Project.create(name, quote)
            print(f'Project {name} has been added')
            view_projects()
            break
        except ValueError as e:
            print(f'Error: {e}')

def selected_project(project_id):
    project = Project.find_by_id(project_id)
    if project:
        name = project.name
        quote = project.quote
        print('\n**************************************************************\n')
        print(f'Project {name} was quoted for ${quote}')
        print('\n')
    else:
        print('\n**************************************************************\n')
        print('Project not found')

def add_expense(project_id):
    while True:
        print('**************************************************************')
        description = input('Please enter expense description: ')
        if not description:
            print('Please enter a valid description')
            continue
        amount = input('Please enter expense amount: ')
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter a valid amount')
            continue
        try:
            Expense.create(description, float(amount), project_id)
            print('The expense has been added')
            break
        except ValueError as e:
            print(f'Error: {e}')

def update_project(project_id):
    while True:
        print('**************************************************************')
        project = Project.find_by_id(project_id)
        name = input('Please enter updated project name or press enter to keep the same: ')
        if name and not name.isdigit():
            project.name = name
        elif not name:
            project.name
        else:
            print('Enter a valid name')
            continue
        quote = input('Please enter updated project quote or press enter to keep the same: ')
        if quote:
            try:
                project.quote = float(quote)
            except ValueError:
                print('Enter a valid quote')
                continue
        if name or quote:
            project.update()
            print('\n**************************************************************\n')
            print(f'Project has been updated to reflect below details:\nProject {project.name} was quoted for ${project.quote}')
            print('\n**************************************************************\n')
            break
        else:
            print('\n**************************************************************\n')
            print('No changes were made')
            print('\n**************************************************************\n')
            break

def view_project_expenses(project_id):
    project = Project.find_by_id(project_id)
    expenses = project.expenses()
    for expense in expenses:
        print(f'{expense.description}: ${expense.amount}')
    print('\n**************************************************************\n')

def delete_project(project_id):
    pass

def exit_program():
    print("Goodbye!")
    exit()
