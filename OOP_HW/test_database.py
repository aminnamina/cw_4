from database_types import MySQLDatabase, PostgreSQLDatabase
from database_connection import DatabaseConnection

if __name__ == "__main__":

    mysql_db = MySQLDatabase()
    db_connection1 = DatabaseConnection(mysql_db)
    result1 = db_connection1.execute_query("SELECT * FROM users")
    print(result1)

    postgres_db = PostgreSQLDatabase()
    db_connection2 = DatabaseConnection(postgres_db)
    result2 = db_connection2.execute_query("SELECT * FROM orders")
    print(result2)

    print("Одинаковые ли экземпляры?", db_connection1 is db_connection2)

    db_connection1.disconnect()
