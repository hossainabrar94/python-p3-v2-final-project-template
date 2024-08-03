# Terraform Construction Bookkeeping

This is a command-line interface (CLI) application for tracking projects and their related expenses. It is designed to help manage construction projects and keep records of expenses in a simple, easy-to-use format. The data is persisted in a SQLite database, ensuring that projects and expenses remain available between sessions.

## Features

- **Project Management**: 
  - Add new projects with a name and quote.
  - Update project details.
  - View all projects.
  - Delete projects.

- **Expense Tracking**: 
  - Add expenses to projects with a description and an amount.
  - View all expenses associated with a specific project.
  - Update expense details.
  - Delete expenses.

---

## Directory Structure

Take a look at the directory structure for this bookkeeping cli application:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── expense.py
    |   └── project.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
    └── seed.py
```
## Getting Started

To get started with the application, follow these steps:

1) Set Up Environment: Ensure you have Python 3.8.13 installed. Create and activate a virtual environment.
pipenv install
pipenv shell

2) Run the Application: Start the CLI application by running:
python lib/cli.py

3) Initialize the Database: Before using the application, ensure the database tables are set up.
python lib/seed.py

4) Usage: Follow the on-screen instructions in the CLI to manage projects and expenses.


## Conclusion

The Terraform Construction Bookkeeping application offers a streamlined solution for managing construction projects and their associated expenses. Its intuitive command-line interface makes it easy to add, update, view, and delete projects and expenses, ensuring efficient bookkeeping for construction activities. This application serves as a practical tool for construction managers and professionals looking to maintain organized and accurate financial records.


## Resources

- https://www.geeksforgeeks.org/enumerate-in-python/
- https://www.w3schools.com/python/ref_func_enumerate.asp
- https://stackoverflow.com/questions/38344194/sql-format-int-to-date-and-add-condition
- https://www.geeksforgeeks.org/difference-between-integer-and-float-in-python/
- https://www.youtube.com/watch?v=4UIYd00J0ok