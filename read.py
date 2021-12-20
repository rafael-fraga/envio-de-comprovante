from pymongo import MongoClient
import pandas as pd


# mongoDB

client = MongoClient('')
db = client['registro-de-entrada']
notas = db['comprovantes']


# pandas

df = pd.DataFrame(list(notas.find({})))
df.drop(['_id'],axis=1, inplace=True)
df = df.iloc[::-1]
result = str(df.to_string(index=False))


print(result)