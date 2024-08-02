from models.__init__ import CURSOR, CONN
from datetime import datetime

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

    # client name must be non-empty string
    @property
    def client(self):
        return self._client
    @client.setter
    def client(self, client):
        if isinstance(client, str) and len(client):
            self._client = client
        else:
            raise ValueError('Must enter clients name')

    # start and end dates must be in date time format    
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if start_date is None:
            self._start_date = None
        else:
            try:
                self._start_date = datetime.strptime(start_date, '%m-%d-%Y')
            except ValueError:
                raise ValueError("Start date must be in 'MM-DD-YYYY' format")
            
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if end_date is None:
            self._end_date = None
        else:
            try:
                self._end_date = datetime.strptime(end_date, '%m-%d-%Y')
            except ValueError:
                raise ValueError("End date must be in 'MM-DD-YYYY' format")

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

    def employees(self):
        pass