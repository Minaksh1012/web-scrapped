
import json
import pprint
def final(text):
    return " ".json(text.split())

def director_analyse():
    list=open("movie details.json")
    language=json.load(list)
    # print(lang)
    list1=[]
    # dict={}
    for i in language:
        # g=i["Original Language:"]

        
        if i["Director:"] not in list1:
            # print(list1)
            list1.append(i["Director:"])
    dict={}
    list2=[]
    for g in list1:
        i=0
        count=0
        while i<len(language):
            if g==final(language[i]["Director:"]):
                count+=1
            i+=1
        dict[g]=count
    # print(dict) 
    pprint.pprint(dict)   



    with open("director.json","w") as f:
        json.dump(dict,f,indent=4)




    # print(list1)
director_analyse()    
