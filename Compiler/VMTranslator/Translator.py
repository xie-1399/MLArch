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

    parser.add_argument("--name",required=True,help="The file path")

    args = parser.parse_args()

    #Convert vm
    parse = Parser(args.name)
    print("clear vmcodes:", parse.clearvmcodes)
    print("parser vmcodeList:",parse.vmcodeList)

    #Write into File

    CodeWriter("./StackTest.asm",parse.vmcodeList)

    print(ContentIsSame("./test/StackTest.asm","./StackTest.asm"))


