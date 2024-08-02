from models.__init__ import CURSOR, CONN

class Project:

    # save all projects
    all_project = {}

    def __init__(self, name, client, location, quote, start_date = None, end_date = None):
        self.name = name
        self.client = client
        self.location = location
        self.quote = quote
        self.start_date = start_date
        self.end_date = end_date

    @property
    def client(self):
        return self._client
    @client.setter
    def client(self, client):
        if isinstance(client, str) and len(client):
            self._client = client
        else:
            raise ValueError('Must enter clients name')
