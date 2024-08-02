from models.__init__ import CONN, CURSOR

class Employee:

    # Save all employees
    all_employees = {}

    def __init__(self):
        pass

    # description of employee
    def __repr__(self):
        pass

    @classmethod
    def create_table(self):
        pass

    @classmethod
    def drop_table(self):
        pass

    def save(self):
        pass

    @classmethod
    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def get_all(self):
        pass

    @classmethod
    def find_by_name(self):
        pass

    def expenses(self):
        pass

    @classmethod
    def project_by_year(self):
        pass