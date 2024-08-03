# lib/helpers.py
from models.expense import Expense
from models.project import Project

def view_projects():
    print("Projects:")
    projects = Project.get_all()
    for project in projects:
        print(f'{project.id}. {project.name}')
    
def add_project():
    name = input("Please enter project's name: ")
    quote = input("Please enter project's quote: ")
    Project.create(name, quote)
    print(f'{name} project has been added')

def selected_project(project_id):
    project = Project.find_by_id(project_id)
    if project:
        name = project.name
        quote = project.quote
        print(f'Project {name} was quoted for ${quote}')
    else:
        print('Project not found')

def add_expense(project_id):
    description = input('Please enter expense description: ')
    amount = input('Please enter expense amount: ')
    Expense.create(description, amount, project_id)
    print('The expense has been added')

def update_project(project_id):
    name = input('Please enter updated project name or press enter to keep the same: ')
    quote = input('Please enter updated project quote or press enter to keep the same: ')
    project = Project.find_by_id(project_id)
    if name:
        project.name = name
    elif quote:
        project.quote = quote

    if name or quote:
        project.update()
        print('Project has been updated')
    else:
        print('No changes were made')

def exit_program():
    print("Goodbye!")
    exit()
