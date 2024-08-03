# lib/helpers.py
from models.expense import Expense
from models.project import Project


# ********************************************************************     Project Functions       ****************************************************************************
def view_projects():
    print('\n**************************************************************\n')
    project_id_map = {}
    projects = Project.get_all()
    if projects:
        print("Projects:")
    else:
        print("Projects:")
        print('No projects have been added')
    for index, project in enumerate(projects, start=1):
        print(f'{index}. {project.name}')
        project_id_map[index] = project.id
    print('\n')
    return project_id_map
    
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
            print('\n**************************************************************\n')
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

def delete_project(project_id):
    project = Project.find_by_id(project_id)
    project.delete()
    print('Project has been deleted')


# ********************************************************************     Expense Functions       ****************************************************************************
def view_project_expenses(project_id):
    project = Project.find_by_id(project_id)
    expenses = project.expenses()
    if expenses:
        print(f'Expenses for project {project.name} below:')
    else:
        print(f'Expenses for project {project.name} below:')
        print('No expense incurred')
    expense_id_map = {}
    for index, expense in enumerate(expenses, start =1):
        print(f'{index}. {expense.description}')
        expense_id_map[index] = expense.id
    print('\n')
    return expense_id_map

def selected_expense(expense_id):
    expense = Expense.find_by_id(expense_id)
    if expense:
        description = expense.description
        amount = expense.amount
        print('\n**************************************************************\n')
        print(f'{description}: ${amount}')
    else:
        print('\n**************************************************************\n')
        print('Expense not found')

def add_expense(project_id):
    while True:
        print('**************************************************************')
        description = input('Please enter expense description: ')
        if not description or description.isdigit():
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
            print('\n**************************************************************\n')
            break
        except ValueError as e:
            print(f'Error: {e}')

def delete_project_expense(expense_id):
    expense = Expense.find_by_id(expense_id)
    expense.delete()
    print('\n**************************************************************\n')
    print('Expense has been deleted')
    print('\n**************************************************************\n')

def update_project_expense(expense_id):
    while True:
        print('**************************************************************')
        expense = Expense.find_by_id(expense_id)
        description = input('Please enter updated description or press enter to keep the same: ')
        if description and not description.isdigit():
            expense.description = description
        elif not description:
            expense.description
        else:
            print('Enter a valid description')
            continue
        amount = input('Please enter updated amount or press enter to keep the same: ')
        if amount:
            try:
                expense.amount = float(amount)
            except ValueError:
                print('Enter a valid amount')
                continue
        if description or amount:
            expense.update()
            print('\n**************************************************************\n')
            print(f'Expense has been updated to reflect below details:\n{expense.description}: ${expense.amount}')
            print('\n**************************************************************\n')
            break
        else:
            print('\n**************************************************************\n')
            print('No changes were made')
            print('\n**************************************************************\n')
            break

def exit_program():
    print("Goodbye!")
    exit()