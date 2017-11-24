import DBUniter
import pickle


def PrintCSV(data, headers, fullFilePath):
    f = open (fullFilePath, "w", encoding = 'utf-8')

    strBuilder = []
    for header in headers:
        strBuilder.append(header+";")
    head = "".join(strBuilder)[:-1]
    f.write(head)

    for d in data:
        strBuilder=["\n"]
        for val in d:
            strBuilder.append(str(val)+";")
        result = "".join(strBuilder)[:-1]
        f.write(result)
    f.close()



query = "SELECT born, retraining_capability FROM cv, old where id = id_cv"
fullPath = "Analysis/RetrainingCspability"
headers = ['born','retraining_capability']

'''db = DBUniter.DBUniter()

print("Executing command")

result = db.Execute(query)
print("Pickle result...")

pickle.dump(result, open(fullPath+".p", "wb"))
print("Done!")'''

result = []
with open(fullPath+".p", 'rb') as f:
    result = pickle.load(f)
PrintCSV(result,headers,fullPath+".csv")