import mysql.connector

db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="050708Sensual",
                                        database="test")
print(db_connection)
db = db_connection.cursor()
# cursor.execute("CREATE TABLE User (Name varchar(255), Email varchar(255), Age int)")

db.execute("INSERT INTO user (Name, Email, Age) VALUES ('Ava', 'ava@gmail.com', 18)")
db_connection.commit()

sql = "SELECT * FROM user"
user = "SELECT * From user where age = 33"
db.execute(user)
users = db.fetchall()
print(users)
