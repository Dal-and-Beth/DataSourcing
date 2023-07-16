from deta import Deta
import pandas as pd

deta = Deta("DB TOKEN HERE")

db = deta.Base("daily_affirmations_test")


def putIntoDB(db):
    df270 = pd.read_excel("../scraping/270Affirmations.xlsx")
    df160 = pd.read_excel("../scraping/160Affirmations.xlsx")

    df160dict = df160.to_dict("list")
    df270dict = df270.to_dict("list")

    for key in df270dict:
        for value in df270dict[key]:
            db.put({"category": key, "text": value})

    for key in df160dict:
        for value in df160dict[key]:
            if pd.isna(value) != True:
                db.put({"category": key, "text": value})


putIntoDB(db)

all_records = db.fetch()
print(type(all_records.items))

new_list = []
for i in all_records.items:
    if i["category"] not in new_list:
        new_list.append(i["category"])

print(new_list)  # sanity check on categories
