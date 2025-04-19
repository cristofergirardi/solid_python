
class DBMysql:
    def connect(self):
        # Simulate a database connection
        print("Connected to the database")

class DBPostgres:
    def connect(self):
        # Simulate a database connection
        print("Connected to the database")

class Model:

    def model_database(self, database: DBMysql):
        """
        Model database
        :param database:
        :return:
        """
        database.connect()

model = Model()
model.model_database(DBMysql())