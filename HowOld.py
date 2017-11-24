import mysql.connector

def CreateConnector(DBName):
    return mysql.connector.connect(user='root', password='',
                                   host='localhost',
                                   database=DBName)


with open("Results/add_old.sql", 'r', encoding='utf-8') as f:
    queries = f.read().split(';')

cnx = CreateConnector('resume15_18')

for query in queries:
    print(query)
    cursor = cnx.cursor()
    cursor.execute(query)
    cursor.close()
    cnx.commit()
cnx.close()