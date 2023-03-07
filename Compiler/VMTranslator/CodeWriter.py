from CommandsTable import *
#将对应的vm命令翻译成Hack汇编代码，需要写入对应的asm文件
#这里可能在A寄存器上行为有一些奇怪，可以想象成是在保护对应的现场一样
#如果是push/pop一个数的流程 （1）把这个数先要存到对应的D寄存器里面去（通过A寄存器） （2）然后对应进栈，栈顶（+-），将之前的Sp值存入A （3）数据进入对应的内存单元
class CodeWriter(object):
    def __init__(self,WriteFile,vmcodeList):
        self.asmwritelist = []
        with open(WriteFile,"w+") as asmfile:
            for vmcode in vmcodeList:
                self.writeArithmetic(vmcode)  #Todo
                self.WritePushPop(vmcode)
            asmfile.write(str(self.asmwritelist))

    #算数操作对应的汇编代码
    def writeArithmetic(self,vmcode):
        if(vmcode[2] == "C_ARITHMETIC"):
            variable = ArithmeticCommands.get(vmcode[3])
            asmArilist = self.ArithmeticTemplate(variable)
            self.asmwritelist.append(asmArilist)
        else:
            return None

    #Just For Pop And Push
    def WritePushPop(self,vmcode):
        if(vmcode[2] == "C_POP"):
            variable = False
            self.asmwritelist.append(self.PushPopTemplate(vmcode[4],variable))
        elif(vmcode[2] == "C_PUSH"):
            variable = True
            self.asmwritelist.append(self.PushPopTemplate(vmcode[4],variable))

    def ArithmeticTemplate(self,variable):
        asmstrlist = ["@SP","AM=M-1","D=M","@SP","AM=M-1",variable,"@SP","M=M+1"]
        return asmstrlist

    def PushPopTemplate(self,number,variable): #Todo
        if(variable):
            asmstrlist = ["@"+str(number),"D=A","@SP","M=M+1","A=M-1","M=D"]  #Push
        else:
            asmstrlist = ["@"+str(number),"D=A","@SP","M=M-1","A=M+1","M=D"]  #Pop
        return asmstrlist
