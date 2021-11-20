from task1 import*
import json
from bs4 import BeautifulSoup
import requests

scrapped=scrape_top_list()


def get_movie_details(movies):

    j=1
    list=[]
    while j<len(movies):
        # print(j)
        newmovielink=movies[j]["movie_link"]
        # print(newmovielink)
        new=newmovielink
        m=requests.get(new)
        # print(m)
        soup=BeautifulSoup(m.text,"html.parser")
        # print(soup)
    
        main=soup.find("ul",class_="content-meta info")
        # print(main)
        all=main.find_all("li",class_="meta-row clearfix")
        # print(all)
        my_dict={}
        for i in all:
            my_dict[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
        # print(my_dict)
        list.append(my_dict)
        # print(list)
        j+=1
    with open("movie details.json","w")as f:
        json.dump(list,f,indent=4)    
        
        # print(soup)
get_movie_details(scrapped)    