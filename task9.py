# from bs4 import BeautifulSoup
# import requests,pprint,json,os,random,time


# def scrap_movie_details(Movie_url):
#     randome_sleep=random.randint(1,3)
#     movi



# a=[1,2,3,4]
# b=[10,20,30,40]
# i=0
# j=1
# while i<len(a):
# #  and i<len(b):
#     print(a[i],b[-j])
#     i+=1
#     j+=1

# a=56
# b=90
# print(a and b)


from task1 import*
import os 
import json
import requests
import random
import time
import pprint
from bs4 import BeautifulSoup



url_list=[]
for i in movies:
    url_list.append(i["movie_link"])
def text_file(ulist):
    last=[]
    time_sleep=random.randint(1,3)
    for i in ulist:
        id=i[33:]
        if os.path.exists("/home/minakshi/Desktop/R/task5.py"+id+".json")==True:
            with open("/home/minakshi/Desktop/R/task5.py"+id+".json","r") as movieDataFile:
                data=movieDataFile.read()
                final=json.loads(data)
            last.append(final)
            time.sleep(time_sleep)
        else:
            final={}
            time.sleep(time_sleep)
            LinkData=requests.get(i)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            final["name"]=soup.find("h1").text
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            for i in all:
                final[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
            with open("/home/minakshi/Desktop/R/task5.py"+id+".json","w") as file:
                json.dump(final,file,indent=2)
            last.append(final)
    return last
pprint.pprint(text_file(url_list))

