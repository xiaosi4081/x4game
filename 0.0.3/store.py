#记得加上creative
import json
def loadthing():
    f = open(r"./whatmai.json","r",encoding="utf-8")
    data = json.load(f)
    f.close()
    return data
def buying(coin,whatihave):
    '''

    有锋利，时运，火焰附加，耐久
      [价格,[锋利值，时运值，火焰附加值，耐久值]]
    '''
    print("欢迎来到SB商店！！！加载货物中...")
    what = loadthing()
    print("属性:[锋利值，时运值，火焰附加值，耐久值]")
    for i in what:
        print(f"装备{i}  ===  ",f"价格：{what[i][0]}","  ",f"属性：{what[i][1]}",sep = "")

    answer = input("你想购买什么装备(输入0即可退出):")
    if answer == "0":
        return
    try:
        price = what[answer][0]
        if coin < price:
            print("SB没钱，快打怪挣钱！")
        else:
            print("成功！")
            coin -= price
            whatihave.setdefault(answer,what[answer])
    except:
        print("没有你SB想要的装备！！！")
        return coin,whatihave
    print("你还剩：",coin)
    return coin,whatihave
def save(data):
    f = open(r"./whatmai.json","w",encoding="utf-8")
    json.dump(data,f)
    f.close()
def creative(password,what):
    if not (password == "qweasd123"):
        print("错误！！")
    ew = input("输入东西名称，价格，锋利值，时运值，火焰附加值，耐久值，用空格隔开：").split(" ")
    try:
        what[ew[0]] = [int(ew[1]),int(ew[2]),int(ew[3]),int(ew[4]),int(ew[5])]
        print(f"创建成功，现在共有{len(what)}件商品，列表：",what)
    except:
        print("Error!You are not enter enongh keys!")
    save(what)
if __name__ == "__main__":
    data = loadthing()
    creative(input("密码："),data)
    #buying(1000,[])