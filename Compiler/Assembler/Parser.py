
#在此部分主要定义，主要实现功能
#如果有循环指令的时候如何对是否还有指令能够进行判断？
import re
class Parse:
    def __init__(self,File):
        self.asmvalidcodelists = []  #Todo 改进一下使用字典
        if (File.endswith("asm")):
            print("Load Asm File")
            with open(File, 'r') as asmfile:
                asmlines = asmfile.readlines()
            self.asmvalidcodes = self.clear(asmlines)  #汇编文件的字符串列表 "HasMoreCommand,advance,commandType,symbol,dest,comp:"
            for i in range(0, len(self.asmvalidcodes)):
                self.asmvalidcodelists.append(self.Process(self.asmvalidcodes))
                self.asmvalidcodes.pop(0)
        else:
            print("The File is Not a Assembler File")

    def Process(self,asmvalidcodes):
        HasMoreCommand = self.hasMoreCommands(asmvalidcodes)
        advance = self.advance(HasMoreCommand,asmvalidcodes)  # 当前执行的指令
        commandType = self.commandType(advance)
        symbol = self.symbol(advance)
        dest_tmp = self.dest(advance)
        if(dest_tmp!=None):
            dest = dest_tmp.rstrip("=")
        else:
            dest = dest_tmp

        comp = self.comp(advance)
        jump = self.jump(advance)
        return HasMoreCommand,advance,commandType,symbol,dest,comp,jump

    def clear(self,asmlines):
        asmvalidcode = []
        for asmline in asmlines:
            if(str(asmline).startswith("//") or str(asmline) == "\n"):
                continue
            else:
                asmline = asmline.rstrip("\n")
                asmline = asmline.replace(" ","")
                asmvalidcode.append(str(asmline))
        return asmvalidcode

    def hasMoreCommands(self,asmvalidcodes):
        if(len(asmvalidcodes) > 0):
            return True
        else:
            return False
    def advance(self,hasMoreCommand,asmvalidcodes):
        #读取下一条指令当作当前的指令
        if(hasMoreCommand):
            advance = asmvalidcodes[0]
            return advance
        else:
            print("Advance Command is None")

    def commandType(self,asmcode):
        if(str(asmcode).startswith("@")): # Todo
            return "A_COMMAND"
        elif(str(asmcode).startswith("(")):
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def symbol(self,asmcode):
        if(self.commandType(asmcode) == "A_COMMAND"):
            return str(bin(int(str(asmcode).lstrip("@")))).replace("0b","")  #Todo
        if(self.commandType(asmcode) == "L_COMMAND"):
            return str(asmcode).lstrip('(').rstrip(')')
        return None

    def dest(self,asmcode):
        if(self.commandType(asmcode) == "C_COMMAND" and str(asmcode).find("=")):  #==左边的符号
            destcode = re.match('.*?=',str(asmcode))
            if(destcode != None):
                return destcode.group()
            else:
                return None
        else:
            return None

    #计算域
    def comp(self,asmcode):
        if(self.commandType(asmcode) == "C_COMMAND"):  #Todo
            if(self.dest(asmcode) is not None):
                asmcode = asmcode.replace(str(self.dest(asmcode)),"")
            if(self.jump(asmcode) is not None):
                asmcode = asmcode.replace(str(self.jump(asmcode)),"")
                asmcode = str(asmcode).rstrip(";")
            return asmcode
        else:
            return None

    def jump(self,asmcode):
        if (self.commandType(asmcode) == "C_COMMAND" and str(asmcode).find(";") != -1):
            return str(asmcode).split(";")[-1]
        else:
            return None

#parse = Parse("./test/Add.asm")