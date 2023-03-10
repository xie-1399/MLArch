#将对应的VM命令转化为对应的asm语言
#v1:算术命令加上内存访问命令，一个比较重要的问题是将操作数和对应的结果存在哪个位置
import argparse


from Parser import *
from CodeWriter import *
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#For Teminal use
from utils.HackCommonUntils import ContentIsSame

#from Compiler.utils.HackCommonUntils import ContentIsSame

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description= "Compile the vm code to the asmcode")

    parser.add_argument("--name",required=False,help="The file path")
    parser.add_argument("--all",required=True,default=False,help="The file path")
    args = parser.parse_args()

    #Write into File
    if(args.all):
        filelist = ["./test/BasicTest.vm","./test/PointerTest.vm","./test/SimpleAdd.vm","./test/SimpleEQ.vm"
            ,"./test/StackTest.vm","./test/StaticTest.vm"]
        for file in filelist:
            parse = Parser(file)
            CodeWriter("./allTest.asm", parse.vmcodeList)
            print(ContentIsSame(file.replace("vm","asm"), "./allTest.asm"))
    else:
        parse = Parser(args.name)
        print("clear vmcodes:", parse.clearvmcodes)
        print("parser vmcodeList:", parse.vmcodeList)
        CodeWriter("./BasicTest.asm",parse.vmcodeList)
        print(ContentIsSame("./test/BasicTest.asm","./BasicTest.asm"))
#Basic Test still has problems  python Translator.py --all 1