from pymongo import MongoClient

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self, connection_string, database):
        self._client = MongoClient(connection_string)
        self._database = self._client[database]
        
    def __call__(self, collection):
        return self._database[collection]
    
    def close(self):
        self._client.close()