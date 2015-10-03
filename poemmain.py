#!/usr/bin/env python3
#-*- coding:utf-8 -*-


__author__="Kairong Zhou"

from class_and_GUI import poem,album
import class_and_GUI as pa
import os
from class_and_GUI import write_poem,scan_poem,create_album,scan_album,rand_poem
    

def main():





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
                optional_func[optional_pick]()
        except:
            print("{} is not a valid input.")




















if __name__=="__main__":
    main()
