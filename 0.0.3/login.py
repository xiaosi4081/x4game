#记得加上whatihave

import json
data = {
    "username":None,
    "live":0,
    "fight":0,
    "unfight":0,
    "run":0,
    "onit":0,
    "level":0,
    "star":0,
    "hu":0,
    "coin":0,
}
def startdata(username,live,fight,unfight,run,onit,level,star,hu,coin,whatihave,pnum):
    f = open(r".\info.json","r",encoding="utf-8")
    jda = json.load(f)
    f.close()
    data["username"]=username
    data["live"]=live
    data["fight"]=fight
    data["unfight"]=unfight
    data["run"]=run
    data["onit"]=onit
    data["level"]=level
    data["star"]=star
    data["hu"]=hu
    data["coin"]=coin
    data["whatihave"]=whatihave
    data["pnum"] = pnum
    for i in range(len(jda['userlist'])):
        if jda['userlist'][i]["username"] == username:
            jda['userlist'].pop(i)
            break
    jda['userlist'].append(data)
    f = open(r".\info.json","w",encoding="utf-8")
    json.dump(jda,f)
    f.close()

def finddata(username):
    f = open(r".\info.json","r",encoding="utf-8")
    jda = json.load(f)
    f.close()
    for i in jda["userlist"]:
        if i["username"] == username:
            return [i["live"],i["fight"],i["unfight"],i["run"],i["onit"],i["level"],i["star"],i["hu"],i["coin"],i["whatihave"],i["pnum"]]
    print("未找到!")
    return 0
