#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from selenium import webdriver


URL1 = "https://www.scienceofpeople.com/positive-affirmations/"
URL2 = "https://www.skillshare.com/en/blog/160-positive-affirmations-for-all-aspects-of-your-life/"
URL3 = "https://www.thegoodtrade.com/features/positive-affirmations-morning-routine/"


def scrape270():
    page = requests.get(URL1)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="post-279007")

    topics = results.find_all("h3")
    affirmations = results.find_all("ol")
    affirmations.pop()

    affirmationsDict = {}

    for index, i in enumerate(affirmations):
        lis = i.find_all("li")
        lis = [li.text for li in lis]
        lis = [li.replace("\xa0", "") for li in lis]

        affirmationsDict[topics[index].text] = lis
    a = pd.DataFrame(affirmationsDict)
    a.to_excel("270Affirmations.xlsx")


def scrape160():
    dr = webdriver.Chrome()
    dr.get(URL2)
    soup = BeautifulSoup(dr.page_source, "html.parser")
    results = soup.find("div", class_="css-svxum1")
    topics = results.find_all("h2", class_="wp-block-heading")
    affirmations = results.find_all("ol")
    del topics[-3:]
    del topics[:2]
    print(len(topics), len(affirmations))
    affirmationsDict = {}
    for index, i in enumerate(affirmations):
        lis = i.find_all("li")
        lis = [li.text for li in lis]
        lis = [li.replace("\xa0", "") for li in lis]

        affirmationsDict[topics[index].text] = lis
    df = pd.DataFrame.from_dict(affirmationsDict, orient="index")
    a = df.transpose()
    print(a)
    a.to_excel("160Affirmations.xlsx")


scrape270()
scrape160()
