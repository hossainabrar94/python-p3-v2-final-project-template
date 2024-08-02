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
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('Must enter a name')

    # quote must be am integer         
    @property
    def quote(self):
        return self._quote
    @quote.setter
    def quote(self, quote):
        if quote is type(int):
            self._quote = quote
        else:
            raise ValueError('Please enter a valid amount')
        
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quote INTEGER)
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
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def find_by_name(cls):
        pass

    def expenses(self):
        pass