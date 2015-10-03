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
    print("*"*50,"\n\n\n\n"," "*25,"Poetry Library\n")
    while True:
        print("1.write your poem")
        print("2.scan all poems")
        print("3.creat your album(诗歌集)")
        print("4.scan all albums")
        print("5.pick random poem")
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
