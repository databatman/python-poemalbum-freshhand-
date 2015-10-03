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
        print("title: %s\npoet: %s"%(self.title,self.poet))
        poemlines=self.text.split('\n')
        for line1 in poemlines:
            print(line1)
            time.sleep(0.9)

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
            album_poem=str(i)+album_poem
            print(album_poem)
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
        return album(p['title'],p['labels'],p['nums'],p['poems'])
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
        write_title=input("please enter poem's name:")
        write_poet=input("please enter poem's poet:")
        print("please enter poem's text.")
        print("PS:注意请在每行诗的末尾加上\\n:")
        write_text=input()
        write_dynasty=input("please enter poem's dynasty[ex:古代,唐宋,元明清,近代]:")
        while True:           
                if write_dynasty in [u"古代",u"唐宋",u"元明清",u"近代"]:
                    break
                else:
                    print("{} is not a valid input.".format(value))
                    write_dynasty=input("please enter right dynasty\[ex:古代,唐宋,元明清,近代]")

        writed_poem=poem(write_title,write_poet,write_text,write_dynasty)
        checkyn=input("Do you want to check your poem just writed?[y/n]:")
        if checkyn=='y':
            print("The poem below is your poem:")
            time.sleep(0.5)
            print(write_poem)
            writed_poem.print_poem()
            qwrite=input("Do you want to make some change?[y/n]:")     
            if qwrite=='n':
                serial_poem(writed_poem)              
                break                                             #之后要提供循环接口

#浏览所有的诗歌
def scan_poem():
    i=0
    scan_poemslist=[x for x in os.listdir(os.path.join(os.path.abspath('.'),'poems'))\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
    for _poemslist in scan_poemslist:
        i+=1
        _poemlist=str(i)+'.'+_poemslist       #在窗口打印所有的诗歌名单
        print(_poemslist)
    while True:
        j=input("Which one do you want to see?[q to exit]:")     #查看指定的诗歌
        if isinstance(j,int) and j>=0 and j<=len(scan_poemslist):
            pick_poem='poems\\'+scan_poemslist[j-1]
            
            picked_poem=unserial_poem(pick_poem)                  #反系列化过程
            picked_poem.print_poem()                              #在桌面打印诗歌
            

        if j=='q':
            pass


#随机诗歌
def rand_poem():
    while True:
        poemslist=[x for x in os.listdir(os.path.join(os.path.abspath('.'),'poems'))\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
        i=randint(0,len(poemslist))
        random_picked=unserial_poem(poemslist[i])
        random_picked.print_poem()

        qcontinue=input("press any key to continue[q to exit]:")
        if qcontinue=='q':
            pass


#已有诗歌集
def scan_album():
    while True:
        i=0
        scan_albumslist=[x for x in os.listdir(os.path.join(os.path.abspath('.'),'albums'))\
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']
        for _albumslist in scan_albumslist:
            i+=1
            _albumslist=str(i)+'.'+_albumslist       #在窗口打印所有的诗歌名单
            print(_albumslist)
            print('q to exit.')
        
        j=input("Which one do you want to see?[q to exit]:")     #查看指定的诗歌
        if isinstance(j,int) and j>=0 and j<=len(scan_albumslist):
            pick_album=scan_albumslist[j-1]            
            picked_album=unserial_album(pick_album)                  #反系列化过程
                                       
            while True:
                picked_album.print_albums()                       #在桌面打印诗歌
                k=input("pick one to read[q to exit]:")
                if isinstance(k,int):
                    pick_album_poem=picked_album.poems[k-1]
                    picked_album_poem=unserial_poem(pick_album_poem)   #打开指定诗歌
                    picked_album_poem.print_poem()
                elif k=='q':
                    break
                else:
                    print("{} is not a valid input.")

        if j=='q':
            break



#创建诗歌集
def create_album():

    while True:

        write_title=input("please enter album's name:")
        write_label=input("please enter album's label[only one]:")
        print("please enter poem's name you want to add:")
        print(os.listdir(os.path.join(os.path.abspath('.'),'poems')))
        print("PS:注意名字必须同上面的目录一样，'.json'也要输入")
        a=1
        while True:                #诗歌名字输入
            input_poem=input("plaese enter 第{}首 name[q to exit]:".format(a))
            input_poem=input_poem.strip()
            if input_poem in os.listdir(os.path.join(os.path.abspath('.'),'poems'):
                a=a+1
                input_poems.append(input_poem)
            elif input_poem=='q':
                break
            else:
                print ("%s is not a valid input."% input_poem)
              
        created_album=album(write_title,write_label,input_poems)
        serial_album(created_album)

        print("Congratulation!You just create an album!Now you can see it in '已有诗歌集'.")
        qcontinue=input("Press q to exit:")
        if qcontinue:
            break

