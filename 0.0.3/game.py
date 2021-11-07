'''
author:Gibbs
v0.0.3

-更新日记
v.0.0.3 - 2021-11-03 ~ 2021-11-07

-增加
    ·在原有的基础上，增加金币、商店、BOSS、技能、仆从兵功能

-优化
    ·优化已知BUG
'''


import random
from login import startdata
from login import finddata
import store
import time



flag = False
class monster:
    live = 0
    fight = 0
    unfight =0
    run = 0
    onit = 0
    def __init__(self,playersum):
        print(playersum)
        self.fight=random.randint(1,playersum//4)
        print(self.fight)
        self.run=random.randint(1,playersum//4)
        print(self.run)
        self.onit=random.randint(1,playersum//4)
        print(self.onit)
        self.unfight=random.randint(1,playersum//4)
        self.live = playersum -(self.fight+self.unfight+self.run+self.onit)
        

class player:

    whatihave = {}
    pnum = 0
    coin = 0
    level = 0
    star = 0
    title = "SBISME"
    live =0
    fight = 0
    unfight =0
    run = 0
    onit = 0
    hu = 25
    def levelup(self):
        if self.star >= 100:
            self.level+=1
            self.hu+=5
            self.star -=100
            print("Wow!你升级了！！！！！！！获得5属性点")
    def save(self):
        startdata(self.title,self.live,self.fight,self.unfight,self.run,self.onit,self.level,self.star,self.hu,self.coin,self.whatihave,self.pnum)
    def started(self,uname):
        if type(finddata(uname))==int:
            print("登录失败！")
            exit(0)
        else:
            listi = finddata(uname)
            print(listi)
            self.title = uname
            self.live = listi[0]
            self.fight=listi[1]
            self.unfight=listi[2]
            self.run=listi[3]
            self.onit=listi[4]
            self.level=listi[5]
            self.star=listi[6]
            self.hu=listi[7]
            self.coin = listi[8]
            self.whatihave = listi[9]
            self.pnum = listi[10]
    def __init__(self,title):
        if not flag:
            if title !=" ":
                self.title = title
            try:
                self.fenpei()
            except:
                print("出错！")
            print("你的用户名是：",self.title)
        else:
            self.started(title)
        print("你好！",self.title)
        while 1:
            try:
                choose = input("你要设置属性点、打怪、修炼、查看信息、购买物品、学习、采矿、还是退出（输入设置属性点/打怪/修炼/退出/查看信息/学习/采矿）：")
                if choose == "设置属性点":
                    self.fenpei()
                elif choose == "修炼":
                    self.exercise()
                elif choose == "打怪":
                    self.fighting()
                elif choose == "查看信息":
                    print("你",self.level,"级了！")
                    print("你的经验值:",self.level*100+self.star)
                    print("你的属性点有",self.hu)
                    print("你有",self.coin,"元")
                elif choose == "购买物品":
                    dt = store.buying(self.coin,self.whatihave)
                    self.coin = dt[0]
                    self.whatihave =dt[1]
                elif choose=="退出":
                    self.save()
                    break
                elif choose == "学习":
                    self.study()
                elif choose == "采矿":
                    self.getk()
                else:
                    print("诶呀，你输入的是什么？")
            except Exception as e:
                print("喵呜！粗错了！",e)
            self.levelup()
    def addsx(self):
        while 1:
            add = int(input("添加多少："))
            if add > self.hu:
                print("加的太大了！")
            elif add < 0:
                print("加的太小了！")
            else:
                self.hu-=add
                return add
    def study(self):
        #       live fight unfight onit run
        data = [[{"小强强":5}],[{"飞踢":5}],[{"铁布衫":10}],[{"豹眼":5}],[{"跃起":5}]]
        print("欢迎来到实力至上主义的课堂！！！在这里，你可以学习技能，并有可能获得仆从兵奖励，学费为100一次")
        chooseyesno = input("是否交钱（T/F）：")
        if chooseyesno == "T":
            self.coin -= 100
            typef = random.randint(0,4)
            num = data[typef][random.randint(0,len(data[typef])-1)]
            for i in num.keys():
                print("恭喜！学习到技能：",i)
                print(typef,num[i])
                if typef == 0:
                    self.live+=num[i]
                elif typef == 1:
                    self.fight+=num[i]
                elif typef == 2:
                    self.unfight += num[i]
                elif typef == 3:
                    self.onit+=num[i]
                elif typef == 4:
                    self.run += num[i]
            if random.randint(1,10)==1:
                print("恭喜获得奖励！1x仆从兵")
                self.pnum+=1
    def fenpei(self):
        while 1:
            choose = int(input("请问你想要分配属性点吗（1/0）,你的属性点有："+str(self.hu)+":"))
            if choose:
                how = input("请问你想分配啥（live/fight/unfight/run/onit）：")
                if how == "live":
                    self.live+=self.addsx()
                elif how=="fight":
                    self.fight+=self.addsx()
                elif how=="unfight":
                    self.unfight+=self.addsx()
                elif how=="run":
                    self.run+=self.addsx()
                elif how == "onit":
                    self.onit+=self.addsx()
                else:
                    print("喵？你输入的是啥？")
                print("分配成功！")
            else:
                return 0
    def exercise(self):
        if random.randint(1,10) == 1:
            print("恭喜你！中奖了！！！获得10经验")
            self.star += 10
        else:
            print("喵呜!没中，下次再努力")
    def isboss(self):
        if random.randint(1,10) == 1:
            print("诶呀！BOSS来啦！打败Boss可获得双倍奖励!")
            return True
        else:
            return False
    def zhuang(self):
        fight = 0
        for i in self.whatihave:
            a = self.whatihave[i][1][0]
            b = self.whatihave[i][1][1]
            c = self.whatihave[i][1][2]
            fight += a//2+(random.randint(b,10)==10) + c//2
            self.whatihave[i][1][3]-=fight//3
        return fight
    def fighting(self):
        suma = 0
        playersum=self.live+self.fight+self.unfight+self.run
        Monster1 = monster(playersum)
        monsterlive = Monster1.live*50+100
        playerlive = self.live*50+100
        flag1 = self.isboss()
        selffight = self.fight+self.zhuang()
        print(self.live,selffight,self.unfight,self.run)
        if flag1:
            Monster1.fight*=1.5
            Monster1.live*=1.5
            Monster1.onit*=1.5
            Monster1.unfight*=1.5
        print("你的生命值是",playerlive,"\n怪物的生命值是",monsterlive)
        if self.pnum != 0:
            print("你的仆从兵给你加了",self.pnum*5,"攻击点")
            selffight+=self.pnum*5
        a = time.time()
        print("请等待！")
        while monsterlive >0 and playerlive>0:
            b= time.time()
            if b-a >= 30:
                break
            #如果我方闪避大于怪物攻击
            if self.run > Monster1.onit:
                if not random.randint(1,100 - self.run - Monster1.onit) == 1:
                    if self.unfight !=0:
                        playerlive -= Monster1.fight // self.unfight
                    else:
                        playerlive -= Monster1.fight
            else:
                if self.unfight !=0:
                    playerlive -= Monster1.fight // self.unfight
                else:
                    playerlive -= Monster1.fight 
            if Monster1.run > self.onit:
                if not random.randint(1,100 - Monster1.run - self.onit) == 1:
                    monsterlive -= selffight // Monster1.unfight
            else:
                monsterlive -= selffight // monster.unfight
            suma+=1
        else:
            if monsterlive<=0:
                if not flag1:
                    self.star+=20
                    addcoin = random.randint(100,200)
                    print("你赢了！一共大战了",suma/2,"回合，","获得",addcoin,"个金币和20经验")
                    self.coin += addcoin
                    return 0
                else:
                    self.star+=40
                    addcoin = random.randint(250,500)
                    print("哇！你战胜了boss，用了",suma/2,"回合,获得",addcoin,"个金币！获得40经验！恭喜！！！")
                    self.coin += addcoin
                    return 0
            if playerlive<=0:
                self.star+=5
                print("你输了！一共大战了",suma/2,"回合")
                return 0
        print("平局！获得50金币参与奖，12个星")
        self.star+=12
        self.coin+=50
    def getk(self):
        kp = {"石头":1,"铜块":3,"铁块":10,"金块":20,"青金石块":30,"钻石":50,"绿宝石":100}
        this = ["石头","铜块","铁块","金块","青金石块","钻石","绿宝石"]
        y = input("是否花费20采矿？(Y/N)")
        if y == "Y":
            self.coin -= 20
            f = this[random.randint(0,len(this)-1)]
            print("你采到了",f,"!","获得：",kp[f],"个金币",sep="")
            self.coin += kp[f]
print("Hello!!!!欢迎来到MC!!!!喵!!!!")
string = input("请输入你的用户名(如果用账号直接输入，没账号的在前面加\"---\"(三条短杠))：")
if string[:3]=="---":
    print("注册成功")
    string =" "
else:
    flag = True
Player1 = player(string)
