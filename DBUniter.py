
import mysql.connector

class DBSelector:
    def CreateConnector(self):
        return mysql.connector.connect(user='root', password='',
                                       host='localhost',
                                       database=self.DBName)
    def __init__(self,dbName):
        self.DBName = dbName

    def Execute(self, query):
        cnx = self.CreateConnector()
        cursor = cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result



class DBUniter:
    Selectors = []
    def __init__(self):
        self.Selectors.append(DBSelector("resume0_2"))
        self.Selectors.append(DBSelector("resume3_5"))
        self.Selectors.append(DBSelector("resume6_8"))
        self.Selectors.append(DBSelector("resume9_11"))
        self.Selectors.append(DBSelector("resume12_14"))
        self.Selectors.append(DBSelector("resume15_18"))
    def Execute(self,query):
        result = []
        for selector in self.Selectors:
            result.extend(selector.Execute(query))
        return result
