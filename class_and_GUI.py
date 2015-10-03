#!/usr/bin/env python3
#-*- coding:utf-8 -*-


'Class of Music Album'


__author__="Kairong Zhou"


from random import randint
import time
import os 
import json


 #定义诗歌对象
class poem(object):               
    def __init__(self,title,poet,text,dynasty=None):
        self.title=title
        self.poet=poet
        self.text=text
        self._dynasty=dynasty

    def __str__(self):
        return "title: %s\npoet: %s"%(self.title,self.poet)

    @property
    def dynasty(self):             #函数名跟变量名最好不要一样，不然会出现递归调用
        return self._dynasty
    @dynasty.setter
    def dynasty(self,value):
        while True:
            
            if value in [u"古代",u"唐宋",u"元明清",u"近代"]:
                self._dynasty=value
                break
            else:
                print("{} is not a valid input.".format(value))
                value=input("please enter right dynasty\[ex:古代,唐宋,元明清,近代]")

    def print_poem(self):
        print('*'*50)
        time.sleep(1)
        print("名字: %s"%(self.title))
        time.sleep(1.5)
        print("诗人: %s" % self.poet)
        time.sleep(1.5)
        print('\n')
        time.sleep(1.5)
        poemlines=self.text.split('+')
        for line1 in poemlines:
            print(line1)
            time.sleep(2)
        print('*'*50)
        time.sleep(0.5)

#定义诗歌集对象
class album(object):           
    def __init__(self,title,labels,poems):
        self.title=title
        self.labels=labels
        self.poems=poems
        self.nums=len(poems)

    def change_title(self,title):
        self.title=title
    def change_labels(self,*args):
        self.labels=list(args)

   
    def print_albums(self):
        print("Album:%s\nnums:%s\n"%(self.title,self.nums))
        i=1
        for album_poem in self.poems:
            album_poem1=str(i)+album_poem
            print(album_poem1)
            i=i+1



#将诗歌对象保存成诗歌json
def serial_poem(obi):
    filename=obi.title+'.json'
    os.chdir(os.path.join(os.path.abspath('.'),'poems'))   #将文件储存到poems目录下
    f=open(filename,'w')
    json.dump(vars(obi),f,indent=2)
    f.close()
    os.chdir(os.path.split(os.path.abspath('.'))[0])       #回到上级目录

 #将诗歌json初始化成诗歌对象
def unserial_poem(openpoem):
    def dict_poem(p):
        return poem(p['title'],p['poet'],p['text'],p['_dynasty'])
    os.chdir(os.path.join(os.path.abspath('.'),'poems'))   #将文件储存到poems目录下
    f=open(openpoem,'r')
    b=json.load(f,object_hook=dict_poem)
    f.close()
    os.chdir(os.path.split(os.path.abspath('.'))[0])       #回到上级目录
    return b

#将诗歌集对象保存成json
def serial_album(obi):
    filename=obi.title+'.json'
    os.chdir(os.path.join(os.path.abspath('.'),'albums'))   #将文件储存到albums目录下
    f=open(filename,'w')
    json.dump(vars(obi),f,indent=2)
    f.close()
    os.chdir(os.path.split(os.path.abspath('.'))[0])       #回到上级目录

 #将诗歌集json初始化成诗歌集对象
def unserial_album(openalbum):
    def dict_album(p):
        return album(p['title'],p['labels'],p['poems'])

    os.chdir(os.path.join(os.path.abspath('.'),'albums'))   #打开albums目录
    f=open(openalbum,'r')
    b=json.load(f,object_hook=dict_album)
    f.close()
    os.chdir(os.path.split(os.path.abspath('.'))[0])       #回到上级目录
    return b



##############################################################################################
##############################################################################################
##########################              GUI FUNCTION                ##########################
##############################################################################################
##############################################################################################


'GUI function'


#写入诗歌
def write_poem():
    while True:
        write_title=input("请输入诗的名字:")
        write_poet=input("请输入诗人:")
        print("*"*50)
        print("请输入诗的内容：.")
        print("PS:注意请在每行诗的末尾加上‘+’后再继续输入下一句诗。:")
        print("ex:鹅,鹅,鹅，+曲项向天歌。+白毛浮绿水，+红掌拨清波。")
        write_text=input()
        write_dynasty=input("请输入诗的朝代序号[ex:1.古代,2.唐宋,3.元明清,4.近代]:")
        while True:           
                if write_dynasty in ["1","2","3","4"]:
                    break
                else:
                    print("{} is not a valid input.".format(write_dynasty))
                    write_dynasty=input("请输入正确的朝代序号[ex:1.古代,2.唐宋,3.元明清,4.近代]:")

        writed_poem=poem(write_title,write_poet,write_text,write_dynasty)
        checkyn=input("Do you want to check your poem just writed?[y/n]:")
        if checkyn=='y':
            print("The poem below is your poem:")
            time.sleep(1)
            writed_poem.print_poem()
            qwrite=input("Do you want to make some change?[y/n]:")    
            if qwrite=='n':
                serial_poem(writed_poem)              
                break                     
        if checkyn!='y':
            break                       
        serial_poem(writed_poem)            #保存书写的诗歌

#浏览所有的诗歌
def scan_poem():
    
    os.chdir(os.path.join(os.path.abspath('.'),'poems'))   #修改路径到poems
    scan_poemslist=[x for x in os.listdir('.')\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
    
    os.chdir('..')                                         #回到上级目录

    while True:
        time.sleep(0.5)
        i=0
        for poemslist1 in scan_poemslist:
            i+=1
            _poemslist1=str(i)+'.'+poemslist1       #在窗口打印所有的诗歌名单
            print(_poemslist1)
    
        j=input("Which one do you want to see?[q to exit]:")     #查看指定的诗歌
        if j=='q':
            break
        try:
            intj=int(j)
            if intj>=0 and intj<=len(scan_poemslist):
                pick_poem=scan_poemslist[intj-1]
                picked_poem=unserial_poem(pick_poem)                  #反系列化过程
                picked_poem.print_poem()                              #在桌面打印诗歌
                print("\n\n")
        except:
            print("{} is not a valid input.".format(j))

        


#随机诗歌
def rand_poem():
    while True:
        os.chdir(os.path.join(os.path.abspath('.'),'poems'))   #修改路径到poems
        poemslist=[x for x in os.listdir('.')\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
        os.chdir('..')                                         #回到上级目录
        i=randint(0,len(poemslist))
        random_picked=unserial_poem(poemslist[i])
        random_picked.print_poem()

        qcontinue=input("press any key to continue random[q to exit]:")
        if qcontinue=='q':
            break




#创建诗歌集
def create_album():

    while True:
        a=1
        input_poems=[]
        write_title=input("请输入诗集的名字:")
        write_label=input("请输入诗集的标签[only one]:")
        print('\n')
        print('*'*50,"")
        print("请输入想添加的诗名:")
        print('目录：',os.listdir(os.path.join(os.path.abspath('.'),'poems')))
        print("PS:注意名字必须同上面的目录一样，.json也要输入")

        while True:                #诗歌名字输入
            input_poem=input("请输入第{}首诗歌名字[q to exit]:".format(a))
            input_poem1=input_poem.strip()
            if input_poem1 in os.listdir(os.path.join(os.path.abspath('.'),'poems')):
                a=a+1
                input_poems.append(input_poem1)
            elif input_poem1=='q':
                break
            else:
                print ("%s is not a valid input."% input_poem)
              
        created_album=album(write_title,write_label,input_poems)
        serial_album(created_album)

        print('*'*50,"\nCongratulation!You just create an album!Now you can see it in '已有诗歌集'.")
        qcontinue=input("Press q to exit:")
        if qcontinue:
            break


#已有诗歌集
def scan_album():
    while True:
        i=0
        os.chdir(os.path.join(os.path.abspath('.'),'albums'))   #修改路径到albums
        scan_albumslist=[x for x in os.listdir('.')\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
        os.chdir('..')
        print("诗歌集：")
        for albumslist in scan_albumslist:
            i+=1
            _albumslist=str(i)+'.'+albumslist       #在窗口打印所有的诗歌名单
            print(_albumslist)
        print('\n')
        j=input("Which one do you want to see?[q to exit]:")     #查看指定的诗歌
        if j=='q':
            break
        try:
            intj=int(j)
            if intj>=0 and intj<=len(scan_albumslist):
                pick_album=scan_albumslist[intj-1]          
                picked_album=unserial_album(pick_album)                  #反系列化过程
                print('\n')               
                while True:
                    print('*'*50) 
                    time.sleep(0.5)
                    picked_album.print_albums()                       #在桌面打印诗歌
                    print('\n')
                    k=input("pick one to read[q to exit]:")
                    if k=='q':
                        break
                    try:
                        intk=int(k)
                        pick_album_poem=picked_album.poems[intk-1]
                        picked_album_poem=unserial_poem(pick_album_poem)   #打开指定诗歌
                        picked_album_poem.print_poem()
                    except:
                        print("%s is not a valid input."% k)
        except:
            print("{} is not a valid input.".format(j))

