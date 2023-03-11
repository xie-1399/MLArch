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
    parser.add_argument("--all",action="store_true",help="run or not")
    args = parser.parse_args()

    #Write into File
    if(args.all):
        filelist = ["./test/BasicTest.vm","./test/PointerTest.vm","./test/SimpleAdd.vm","./test/SimpleEQ.vm"
            ,"./test/StackTest.vm","./test/StaticTest.vm","./test/BasicLoop.vm","./test/FibonacciSeries.vm"]
        for file in filelist:
            parse = Parser(file)
            filename = file.split('/')[-1].replace(".vm","")
            CodeWriter("./allTest.asm", parse.vmcodeList,filename)
            print(ContentIsSame(file.replace("vm","asm"), "./allTest.asm"))
    else:
        parse = Parser(args.name)
        filename = str(args.name).split('/')[-1].replace(".vm","")
        print("clear vmcodes:", parse.clearvmcodes)
        print("parser vmcodeList:", parse.vmcodeList)
        CodeWriter("./BasicTest.asm",parse.vmcodeList,filename)
        print(ContentIsSame(str(args.name).replace("vm","asm"),"./BasicTest.asm"))
#Basic Test still has problems  python Translator.py --all 1