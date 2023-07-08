#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

URL1 = "https://www.scienceofpeople.com/positive-affirmations/"
URL2 = "https://www.skillshare.com/en/blog/160-positive-affirmations-for-all-aspects-of-your-life/"
URL3 = "https://www.thegoodtrade.com/features/positive-affirmations-morning-routine/"


def firstUrlScrape():
    page = requests.get(URL1)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="post-279007")
    # affirmations = results.find_all("div", class_="entry-content")

    topics = results.find_all("h3")
    affirmations = results.find_all("ol")
    affirmations.pop()
    # li = results.find("")/
    # li = affirmations.

    affirmationsDict = {}

    for index, i in enumerate(affirmations):
        lis = i.find_all("li")
        lis = [li.text for li in lis]
        # print(lis)
        affirmationsDict[topics[index].text] = lis
        # for il in ils:
        #     affirmationsDict[index] = il

        # print(il.text, end=" ")
        # print(index)
        # print(j.text, end=" ")
    a = pd.DataFrame(affirmationsDict)
    # print(a)
    a.to_excel("Affirmations.xlsx")


firstUrlScrape()
# with open("affirmations.txt", "w") as file:
#     file.write(json.dumps(affirmationsDict))
# print(affirmationsDict.pop(len(affirmationsDict) - 1))
# print(affirmationsDict)
# print(len(topics))
# print(len(affirmations))
# print(results.prettify())
# for i in affirmations:
# topic = i.find("h3")

# print(page.text)

# BeautifulSoup.
