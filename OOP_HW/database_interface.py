from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute_query(self, query: str):
        pass
    @abstractmethod
    def disconnect(self):
        pass