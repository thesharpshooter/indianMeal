from bs4 import BeautifulSoup as bs
import requests
url = "http://www.indianfoodforever.com/"
data = requests.get(url).text
soup = bs(data,"html5lib")
tag1 = soup.findAll('li',{"class":"cat-item flinks"})
tag2 = soup.findAll("li",{"class":"cat-item links level2recipelinks"})
mealType = []
meal = []
for t in tag1:
    mealType.append(t.a["href"])
for t in tag2:
    mealType.append(t.a["href"])
i = 0
for url in mealType:
    data = requests.get(url).text
    soup = bs(data,"html5lib")
    tag1 = soup.findAll("div",{"class":"one-third first"})
    tag2 = soup.findAll("div",{"class":"one-third"})
    for t in tag1:
        ref = t.findAll("a")
        for a in ref:
            print "got meal ",i," --> ",a.string
            meal.append(a.string)
            i += 1
with open("meals.txt" ,"w") as f:
    for x in meal :
        f.write(x+" ")

