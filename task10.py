import json

with open("movie details.json","r") as f:
    data1=json.load(f)

def language_and_directores(movies_list):
    DirectoresDict={}
    for movies in movies_list:
        for Director in movies:
            if Director=="Director:":
                DirectoresDict[movies[Director]]={}
    for i in range(len(movies_list)):
        for Director in DirectoresDict:
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        a=movies_list[i]["Original Language:"]
                        DirectoresDict[Director][a]=0
    for i in range(len(movies_list)):
        for Director in DirectoresDict:
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        for l in DirectoresDict[Director]:
                            DirectoresDict[Director][l]+=1
    return DirectoresDict

Director_language=language_and_directores(data1)
with open("DirectorByLanguage.json","w") as f:
    json.dump(Director_language,f,indent=4)
# print(Director_language)