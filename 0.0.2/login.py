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
    "hu":0
}
def startdata(username,live,fight,unfight,run,onit,level,star,hu):
    f = open(r"E:\4\华景信息技术校队\python\6game\0.0.2\info.json","r",encoding="utf-8")
    jda = json.load(f)
    f.close()
    data["username"]=username
    data["live"]=live
    data["fight"]=fight
    data["unfight"]=unfight
    data["run"]=run
    data["level"]=level
    data["star"]=star
    data["onit"]=onit
    data["hu"]=hu
    jda['userlist'].append(data)
    f = open(r"E:\4\华景信息技术校队\python\6game\0.0.2\info.json","w",encoding="utf-8")
    json.dump(jda,f)
    f.close()

def finddata(username):
    f = open(r"E:\4\华景信息技术校队\python\6game\0.0.2\info.json","r",encoding="utf-8")
    jda = json.load(f)
    f.close()
    for i in jda["userlist"]:
        print(i)
        if i["username"] == username:
            return [i["live"],i["fight"],i["unfight"],i["run"],i["level"],i["star"],i["onit"],i["hu"]]
    print("未找到!")
    return 0