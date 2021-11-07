'''
author:Gibbs
v0.0.2

-更新日记
v.0.0.2 - 2021-10-26

-增加
    在原有的基础上，增加 json 登录环节
'''


import random
from login import startdata
from login import finddata

flag = False

class monster:
    live = 0
    fight = 0
    unfight =0
    run = 0
    onit = 0
    def __init__(self,playersum):
        self.fight=random.randint(1,playersum//4)
        self.run=random.randint(1,playersum//4)
        self.onit=random.randint(1,playersum//4)
        self.unfight=random.randint(1,playersum//4)
        self.live = playersum -(self.fight+self.unfight+self.run+self.onit)
        

class player:
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
        startdata(self.title,self.live,self.fight,self.unfight,self.run,self.onit,self.level,self.star,self.hu)
    def started(self,uname):
        if type(finddata(uname))==int:
            print("登录失败！")
            exit(0)
        else:
            listi = finddata(uname)
            self.title = uname
            self.live = listi[1-1]
            self.fight=listi[2-1]
            self.unfight=listi[3-1]
            self.run=listi[4-1]
            self.onit=listi[5-1]
            self.level=listi[6-1]
            self.star=listi[7-1]
            self.hu=listi[8-1]
    def __init__(self,title):
        if not flag:
            if title !=" ":
                self.title = title
            print("你的用户名是：",self.title)
        print("你好！",self.title)
        if not flag:
            try:
                self.fenpei()
            except:
                print("出错！")
        else:
            self.started(title)
        while 1:
            try:
                choose = input("你要设置属性点,打怪,修炼,查看信息还是退出（输入设置属性点/打怪/修炼/退出/查看信息）：")
                if choose == "设置属性点":
                    self.fenpei()
                elif choose == "修炼":
                    self.exercise()
                elif choose == "打怪":
                    self.fighting()
                elif choose == "查看信息":
                    print("你",self.level,"级了！")
                    print("你的经验值",self.level*100+self.star)
                    print("你的属性点有",self.hu)
                elif choose=="退出":
                    self.save()
                    break
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
        
    def fighting(self):
        suma = 0
        playersum=self.live+self.fight+self.unfight+self.run
        Monster1 = monster(playersum)
        monsterlive = Monster1.live*50+100
        playerlive = self.live*50+100
        print("你的生命值是",playerlive,"\n怪物的生命值是",monsterlive)
        while monsterlive >0 and playerlive>0:
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
                    monsterlive -= self.fight // Monster1.unfight

            else:
                monsterlive -= self.fight // monster.unfight
            suma+=1
        if monsterlive<=0:
            self.star+=20
            print("你赢了！一共大战了",suma/2,"回合")
        if playerlive<=0:
            self.star+=5
            print("你输了！一共大战了",suma/2,"回合")

print("Hello!!!!欢迎来到MC!!!!喵!!!!")
string = input("请输入你的用户名(如果用账号直接输入，没账号的在前面加\"---\"(三条短杠))：")
if string[:3]=="---":
    print("注册成功")
    string =" "
else:
    flag = True
Player1 = player(string)

