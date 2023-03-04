#将对应的VM命令转化为对应的asm语言
#v1:算术命令加上内存访问命令，一个比较重要的问题是将操作数和对应的结果存在哪个位置
import argparse
from Parser import *
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description= "Compile the vm code to the asmcode")

    parser.add_argument("--name",required=True,help="The file path")

    args = parser.parse_args()

    #Convert vm
    parse = Parser(args.name)
