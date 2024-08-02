from models.__init__ import CONN,CURSOR

class Trade:

    # save all trades
    all_trades = {}

    def __init__(self, name, id=None):
        pass

    @classmethod
    def create_table(cls):
        pass

    @classmethod
    def drop_table(cls):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def get_all_trades(cls):
        pass

    @classmethod
    def find_by_name(cls):
        pass

    def employees(self):
        pass