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
from utils.HackCommonUntils import ContentIsSame,judgeBoot

#from Compiler.utils.HackCommonUntils import ContentIsSame

#Todo if the file stratswith sys(引导程序代码需要将堆栈的地址编译到256)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description= "Compile the vm code to the asmcode")
    parser.add_argument("--name",required=False,help="The file path")
    parser.add_argument("--all",action="store_true",help="run or not")
    args = parser.parse_args()

    #Write into File
    if(args.all):
        filelist = ["./test/BasicTest.vm","./test/PointerTest.vm","./test/SimpleAdd.vm","./test/SimpleEQ.vm"
            ,"./test/StackTest.vm","./test/StaticTest.vm","./test/BasicLoop.vm","./test/FibonacciSeries.vm",
            "./test/SimpleFunction.vm","./test/Sysfibo.vm","./test/SysClass.vm"]
        filepath = "./test/"
        allfiles = os.listdir(filepath)
        allfiles.sort()
        for file in filelist:
            parseTemplist = []
            boot = judgeBoot(file)
            if(boot):
                parse = Parser(file)
                filename = file.split('/')[-1].replace(".vm", "")
                filecontactname = filename.lstrip("Sys")
                for filecontact in allfiles:
                    if(filecontact.startswith(filecontactname) and filecontact.endswith(".vm")):
                        targetfilepath = filecontact
                        parseTemp = Parser(filepath + targetfilepath)
                        parseTemplist.extend(parseTemp.vmcodeList)  #No Return value
                parseTemplist.extend(parse.vmcodeList)
                CodeWriter("./allTest.asm", parseTemplist, filename,boot)
                print(ContentIsSame(file.replace("vm", "asm"), "./allTest.asm"))
            else:
                parse = Parser(file)
                filename = file.split('/')[-1].replace(".vm","")
                CodeWriter("./allTest.asm", parse.vmcodeList,filename,boot)
                print(ContentIsSame(file.replace("vm","asm"), "./allTest.asm"))

    else:
        filepath = "./test/"
        allfiles = os.listdir(filepath)
        allfiles.sort()
        boot = judgeBoot(args.name)
        parse = Parser(args.name)
        parseTemplist = []
        filename = str(args.name).split('/')[-1].replace(".vm", "")
        if(boot):
            filecontactname = filename.lstrip("Sys")
            for filecontact in allfiles:
                if (filecontact.startswith(filecontactname) and filecontact.endswith(".vm")):
                    targetfilepath = filecontact
                    parseTemp = Parser(str(filepath + targetfilepath))
                    parseTemplist.extend(parseTemp.vmcodeList)  #Todo about the sequence (use sort?)
            parseTemplist.extend(parse.vmcodeList)
            #Maybe more than one file
            print("all vmcodes:",parseTemplist)
            CodeWriter("./singfileTest.asm", parseTemplist, filename, boot)
            print(ContentIsSame(str(args.name).replace("vm", "asm"), "./singfileTest.asm"))
        else:
            parse = Parser(args.name)
            filename = str(args.name).split('/')[-1].replace(".vm","")
            print("clear vmcodes:", parse.clearvmcodes)
            print("parser vmcodeList:", parse.vmcodeList)
            CodeWriter("./singfileTest.asm",parse.vmcodeList,filename,boot)
            print(ContentIsSame(str(args.name).replace("vm","asm"),"./singfileTest.asm"))
