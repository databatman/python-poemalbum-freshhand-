#!/usr/bin/env python3
#-*- coding:utf-8 -*-


__author__="Kairong Zhou"

from class_and_GUI import poem,album
import class_and_GUI as pa
import os
from class_and_GUI import write_poem,scan_poem,create_album,scan_album,rand_poem
    

def main():


#init 最开始需要新建两个文件夹：poems 和 albums
#     判断有则无需新建，没有则在当下目录新建两个

    file1='poems'
    file2='albums'
    if file1 not in os.listdir('.'):
        os.mkdir('poems')
    if file2 not in os.listdir('.'):
        os.mkdir('albums')


    P1=poem('断章','卞之琳','你站在桥上看风景，+看风景人在楼上看你。\
            +明月装饰了你的窗子，+你装饰了别人的梦。','4')    
    P2=poem('错误','郑愁予','我打江南走过+那等在季节里的容颜如莲花的开落\
            + +东风不来，三月的柳絮不飞+你底心如小小寂寞的城+恰若青石的街道向晚\
            +蛰音不响，三月的春帷不揭+你底心是小小的窗扉紧掩+ +我达达的马蹄是美丽的错误\
            +我不是归人，是个过客…','4')
    P3=poem('等你，在雨中','余光中','等你，在雨中，在造虹的雨中+蝉声沉落，蛙声升起\
            +一池的红莲如红焰，在雨中+你来不来都一样，竟感觉+每朵莲都像你\
            +尤其隔着黄昏，隔着这样的细雨+永恒，刹那，刹那，永恒+等你，在时间之外，在时间之内，\
            +等你+在刹那，在永恒+如果你的手在我的手里，此刻+如果你的清芬\
            +在我的鼻孔，我会说，小情人+诺，这只手应该采莲，在吴宫+这只手应该\
            +摇一柄桂桨，在木兰舟中+一颗星悬在科学馆的飞檐+耳坠子一般的悬着\
            +瑞士表说都七点了+忽然你走来+步雨后的红莲，翩翩，你走来+像一首小令\
            +从一则爱情的典故里你走来+从姜白石的词里，有韵地，你走来','4')
    P4=poem('笑','林徽因','笑的是她的眼睛，口唇， +和唇边浑圆的漩涡。 +艳丽如同露珠，\
            +朵朵的笑向 +贝齿的闪光里躲。 +那是笑——神的笑，美的笑： +水的映影，风的轻歌。\
            + +笑的是她惺松的鬈发， +散乱的挨着她耳朵。 +轻软如同花影， +痒痒的甜蜜 \
            +涌进了你的心窝。 +那是笑——诗的笑，画的笑： +云的留痕，浪的柔波.','4')
    P5=poem('我的名字','普希金','我的名字对你有什么意义？ +它会死去， +像大海拍击海堤，\
            +发出的忧郁的汩汩涛声， +像密林中幽幽的夜声。 + +它会在纪念册的黄页上 \
            +留下暗淡的印痕， +就像用无人能懂的语言 +在墓碑上刻下的花纹。 + \
            +它有什么意义？ +它早已被忘记 +在新的激烈的风浪里，+它不会给你的心灵 \
            +带来纯洁、温柔的回忆。 + +但是在你孤独、悲伤的日子， +请你悄悄地念一念我的名字，\
            +并且说：有人在思念我， +在世间我活在一个人的心里。','1')
    P6=poem('门前','顾城','我多么希望，有一个门口+早晨，阳光照在草上+我们站着\
            +扶着自己的门扇+门很低，但太阳是明亮的+草在结它的种子+风在摇它的叶子\
            +我们站着，不说话+就十分美好+有门，不用开开+是我们的，就十分美好','4')
    P7=poem('你还在我身旁','无名','瀑布的水逆流而上+蒲公英种子从远处飘回，聚成伞的模样，\
            +太阳从西边升起，落向东方。+ +子弹退回枪膛，+运动员回到起跑线，\
            +我交回录取通知书，忘了十年寒窗。+ +厨房里飘来饭菜的香，\
            +你把我的卷子签好名字，关掉电视，+帮我把书包背上。+ +你还在我身旁。','4')
    P8=poem('妈妈钟','小民','当你失望而回时,+孩子，+无论你是多么高，妈妈的胸怀还能将你环绕。\
            +我愿做你的「妈妈钟」，直到钟老炼断没有停摆的一天。')
    pa.serial_poem(P1)
    pa.serial_poem(P2)
    pa.serial_poem(P3)
    pa.serial_poem(P4)
    pa.serial_poem(P5)
    pa.serial_poem(P6)
    pa.serial_poem(P7)
    pa.serial_poem(P8)


    A1=album('微情诗','直戳心灵',['我的名字.json','断章.json','笑.json'\
            ,'等你，在雨中.json','错误.json','门前.json'])
    A2=album('母亲','思念',['你还在我身旁.json','妈妈钟.json'])
    pa.serial_album(A1)
    pa.serial_album(A2)




    optional_func={1:write_poem,2:scan_poem,3:create_album,4:scan_album,5:rand_poem}
    name=input("Please enter you name first:")
    print ("*"*50)
    print ("Welcome {} to use this Poetry Library.".format(name))
    continue_key=input("Now press any key to continue: ")
    print("*"*50,"\n\n\n\n"," "*20,"Poetry Library of {}\n".format(name))
    while True:
        print("\n1.写入诗歌")
        print("2.浏览所有的诗")
        print("3.创建诗歌集")
        print("4.浏览已有诗歌集")
        print("5.选取一首随机的诗")
        print("press num to enter/q to exit.")
        optional_pick=input()
        if optional_pick=='q':
            break
        try:
            optional_pick=int(optional_pick)
            if optional_pick<=5 and optional_pick>=1:
                optional_func[optional_pick]()       #利用键的功能进入各个函数，相当于C++的which-case
        except:
            print("{} is not a valid input.".format(optional_pick))



if __name__=="__main__":
    main()
