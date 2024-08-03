from models.__init__ import CONN, CURSOR
from models.project import Project
from models.expense import Expense

def seed_database():
    Project.drop_table()
    Expense.drop_table()
    Expense.create_table()
    Project.create_table()

    # Create seed data
    john = Project.create("John", "14900")
    calvin = Project.create("Calvin", "18000")
    Expense.create("Material", "450", john.id)
    Expense.create("Disposal", "350.99", john.id)
    Expense.create("Labor", "1200", calvin.id)
    Expense.create("Transportation", "150", calvin.id)
    Expense.create("Material", "1500", calvin.id)


seed_database()
print("Seeded database")
