import threading
from database_interface import DatabaseInterface

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, database: DatabaseInterface):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseConnection, cls).__new__(cls)
                cls._instance.database = database
                cls._instance.database.connect()
        return cls._instance

    def execute_query(self, query: str):
        return self.database.execute_query(query)

    def disconnect(self):
        self.database.disconnect()
