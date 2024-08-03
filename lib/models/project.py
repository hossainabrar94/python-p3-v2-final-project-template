from models.__init__ import CURSOR, CONN

class Project:

    # save projects
    all = {}

    def __init__(self, name, quote, id = None):
        self.id = id
        self.name = name
        self.quote = quote

    # name must be non-empty string
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) and not name.isdigit():
            self._name = name
        else:
            raise ValueError('Must enter a valid name')

    # quote must be an integer         
    @property
    def quote(self):
        return self._quote
    @quote.setter
    def quote(self, quote):
        if isinstance(quote, (int,float)) and quote >0:
            self._quote = quote
        else:
            raise ValueError('Please enter a valid amount')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quote REAL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS projects;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO projects (name, quote)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.quote))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, quote):
        project = cls(name, quote)
        project.save()
        return project

    def update(self):
        sql = """
            UPDATE projects
            SET name = ?,
            quote = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.quote, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM projects
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        project = cls.all.get(row[0])

        if project:
            project.name = row[1]
            project.quote = row[2]
        else:
            project = cls(row[1], row[2])
            project.id = row[0]
            cls.all[project.id] = project
        return project
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM projects
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM projects
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def expenses(self):
        from models.expense import Expense
        sql = """
            SELECT * from expenses
            WHERE project_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Expense.instance_from_db(row) for row in rows]
    
    # @classmethod
    # def find_by_name(cls, name):
    #     sql = """
    #         SELECT * FROM projects
    #         WHERE name = ?
    #     """
    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     return cls.instance_from_db(row) if row else None