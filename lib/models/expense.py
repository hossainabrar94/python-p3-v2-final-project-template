from models.__init__ import CONN, CURSOR

class Expense:

    all = {}

    def __init__(self, description, amount, project_id, id = None):
        self.description = description
        self.amount = amount
        self.project_id = project_id
        self.id = id

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if len(description):
            self._description = description
        else:
            raise ValueError('Please enter a description')
        
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self._amount = amount
        else:
            raise ValueError('Please enter a valid amount')
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT,
            amount REAL,
            project_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS expenses
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO expenses (description, amount, project_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.description, self.amount, self.project_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, description, amount, project_id):
        expense = cls(description, amount, project_id)
        expense.save()
        return expense

    @classmethod
    def instance_from_db(cls, row):
        expense = cls.all.get(row[0])
        if expense:
            expense.description = row[1]
            expense.amount = row[2]
            expense.project_id = row[3]
        else:
            expense = cls(row[1], row[2], row[3])
            expense.id = row[0]
            cls.all[expense.id] = expense
        return expense
    
    def update(self):
        sql = """
            UPDATE expenses
            SET description = ?, amount = ?, project_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.description, self.amount, self.project_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM expenses
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def get_project(self):
        from models.project import Project
        sql = """
            SELECT * FROM projects
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (self.project_id, )).fetchone()
        return Project.instance_from_db(row)
    
    # @classmethod
    # def find_by_description(cls, description):
    #     sql = """
    #         SELECT * FROM expenses
    #         WHERE description = ?
    #     """
    #     row = CURSOR.execute(sql, (description,)).fetchone()
    #     return cls.instance_from_db(row) if row else None