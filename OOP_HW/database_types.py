from database_interface import DatabaseInterface


class MySQLDatabase(DatabaseInterface):
    def connect(self):
        print("Подключение к MySQL")

    def execute_query(self, query: str):
        print(f"Выполнение запроса в MySQL: {query}")
        return "Результат из MySQL"

    def disconnect(self):
        print("Отключение от MySQL")


class PostgreSQLDatabase(DatabaseInterface):
    def connect(self):
        print("Подключение к PostgreSQL")

    def execute_query(self, query: str):
        print(f"Выполнение запроса в PostgreSQL: {query}")
        return "Результат из PostgreSQL"

    def disconnect(self):
        print("Отключение от PostgreSQL")
