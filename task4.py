from task1 import*
import json


def scrape_movie_details(Movie_url):
    moviedetails={}
    page=requests.get(Movie_url)
    # print(page)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    # title_div=soup.find(div,class_="scoreboard_title").h1.get.text()
    # print(title_div)
    moviedetails["name"]=soup.find("h1").text
    # print(moviedetails)
    main=soup.find("ul",class_="content-meta info")
    # print(main)
    all=main.find_all("li",class_="meta-row clearfix")
    # print(all)
    for i in all:
        # print(i)
        moviedetails[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
        # print(moviedetails)
    with open("blackpantherMovieDetails.json","w")as f:
        json.dump(moviedetails,f,indent=4)    


scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")    