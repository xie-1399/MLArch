from CommandsTable import *
#将对应的vm命令翻译成Hack汇编代码，需要写入对应的asm文件
#这里可能在A寄存器上行为有一些奇怪，可以想象成是在保护对应的现场一样
#如果是push/pop一个数的流程 （1）把这个数先要存到对应的D寄存器里面去（通过A寄存器） （2）然后对应进栈，栈顶（+-），将之前的Sp值存入A （3）数据进入对应的内存单元
class CodeWriter(object):
    def __init__(self,WriteFile,vmcodeList,filename):
        self.asmwritelist = []
        self.eqcounter = 0
        self.filename = filename
        with open(WriteFile,"w+") as asmfile:
            for vmcode in vmcodeList:
                self.writeArithmetic(vmcode)  #Todo
                self.writePushPop(vmcode)
                self.writeLabel(vmcode)
                self.writeGoto(vmcode)
                self.writeIFGoto(vmcode)
            asmfile.write(str(self.asmwritelist))

    #算数操作对应的汇编代码
    def writeArithmetic(self,vmcode):
        if(vmcode[2] == "C_ARITHMETIC"):
            arithType = ArithmeticType.get(vmcode[3])
            variable = ArithmeticCommands.get(vmcode[3])
            asmArilist = self.ArithmeticTemplate(variable,arithType)
            self.asmwritelist.append(asmArilist)
        else:
            return None

    def writeLabel(self,vmcode):
        if(vmcode[2] == "C_LABEL"):
            variable = vmcode[3] #Label Name
            asmLabellist = self.LabelTemplate(variable,self.filename)
            self.asmwritelist.append(asmLabellist)
        else:
            return None

    def writeGoto(self,vmcode):
        if (vmcode[2] == "C_GOTO"):
            variable = vmcode[3]
            asmgotolist = self.GotoTemplate(variable,self.filename)
            self.asmwritelist.append(asmgotolist)
        else:
            return None
    def writeIFGoto(self,vmcode):
        if (vmcode[2] == "C_IF"):
            variable = vmcode[3]
            asmifgotolist = self.IFGotoTemplate(variable,self.filename)
            self.asmwritelist.append(asmifgotolist)
        else:
            return None

    #Just For Pop And Push
    def writePushPop(self,vmcode):
        if(vmcode[2] == "C_POP"):
            popOrpushType = memoryAccessType.get(vmcode[3])
            variable = False
            self.asmwritelist.append(self.PushPopTemplate(vmcode[4],variable,popOrpushType))
        elif(vmcode[2] == "C_PUSH"):
            popOrpushType = memoryAccessType.get(vmcode[3])
            variable = True
            self.asmwritelist.append(self.PushPopTemplate(vmcode[4],variable,popOrpushType))

    def LabelTemplate(self,variable,filename):
        asmstrlist = ["({filename}.main${variable})".format(filename =filename,variable = variable)]
        return asmstrlist

    def GotoTemplate(self,variable,filename):
        asmstrlist = ["@{filename}.main${variable}".format(filename =filename,variable = variable),"0;JMP"]
        return asmstrlist
    def IFGotoTemplate(self,variable,filename):
        asmstrlist = ['@SP', 'AM=M-1', 'D=M', '@1', 'D=D+A', '@{filename}.main${variable}'.format(filename =filename,variable = variable), 'D;JNE']
        return asmstrlist

    def ArithmeticTemplate(self,variable,arithType):
        asmstrlist = []
        match arithType:
            case 0|1:
                asmstrlist = ["@SP","AM=M-1","D=M","@SP","AM=M-1",variable,"@SP","M=M+1"]
            case 2:
                asmstrlist = ['@SP', 'A=M-1', 'M=-M']
            case 3:
                asmstrlist = [ "@SP","M=M-1","A=M","D=M","@SP","M=M-1","A=M","D=D-M","@COND.FALSE.{eqcount}".format(eqcount= self.eqcounter),
                               "D;JNE","@SP","A=M","M=-1", "@COND.TRUE.{eqcount}".format(eqcount= self.eqcounter),"0;JMP",
                               "(COND.FALSE.{eqcount})".format(eqcount= self.eqcounter),"@SP","A=M","M=0","(COND.TRUE.{eqcount})".format(eqcount= self.eqcounter),
                               "@SP","M=M+1"]
                self.eqcounter += 1
            case 4:

                asmstrlist = ['@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'M=D', '@SP', 'M=M-1', 'A=M', 'D=M', '@R14', 'M=D', '@R14', 'D=M', '@GT.XPOS.{eqcount}'.format(eqcount= self.eqcounter),
                               'D;JGT', '@GT.XNEG.{eqcount}'.format(eqcount= self.eqcounter), 'D;JLT', '@GT.NO.OF.{eqcount}'.format(eqcount= self.eqcounter), '0;JMP', '(GT.XPOS.{eqcount})'.format(eqcount= self.eqcounter), '@R13', 'D=M', '@GT.XPOS.YNEG.{eqcount}'.format(eqcount= self.eqcounter), 'D;JLT',
                               '@GT.NO.OF.{eqcount}'.format(eqcount= self.eqcounter), '0;JMP', '(GT.XNEG.{eqcount})'.format(eqcount= self.eqcounter), '@R13', 'D=M', '@GT.XNEG.YPOS.{eqcount}'.format(eqcount= self.eqcounter), 'D;JGT', '(GT.NO.OF.{eqcount})'.format(eqcount= self.eqcounter), '@R13', 'D=M', '@R14',
                               'D=M-D', '@GT.FALSE.{eqcount}'.format(eqcount= self.eqcounter), 'D;JLE', '@SP', 'A=M', 'M=-1', '@GT.TRUE.{eqcount}'.format(eqcount= self.eqcounter), '0;JMP', '(GT.FALSE.{eqcount})'.format(eqcount= self.eqcounter), '@SP', 'A=M', 'M=0', '(GT.TRUE.{eqcount})'.format(eqcount= self.eqcounter),
                               '@GT.END.{eqcount}'.format(eqcount= self.eqcounter), '0;JMP', '(GT.XNEG.YPOS.{eqcount})'.format(eqcount= self.eqcounter), '@SP', 'A=M', 'M=0', '@GT.END.{eqcount}'.format(eqcount= self.eqcounter), '0;JMP', '(GT.XPOS.YNEG.{eqcount})'.format(eqcount= self.eqcounter), '@SP', 'A=M', 'M=-1', '(GT.END.{eqcount})'.format(eqcount= self.eqcounter), '@SP', 'M=M+1']
                self.eqcounter += 1

            case 5:
                asmstrlist = ["@SP","M=M-1","A=M","D=M","@R13","M=D","@SP","M=M-1","A=M","D=M","@R14","M=D",
                             "@R14","D=M","@LT.XNEG.{eqcount}".format(eqcount= self.eqcounter),"D;JLT","@LT.XPOS.{eqcount}".format(eqcount= self.eqcounter),"D;JGT","@LT.NO.OF.{eqcount}".format(eqcount= self.eqcounter),"0;JMP",
                              "(LT.XNEG.{eqcount})".format(eqcount= self.eqcounter),"@R13","D=M","@LT.XNEG.YPOS.{eqcount}".format(eqcount= self.eqcounter),"D;JGT","@LT.NO.OF.{eqcount}".format(eqcount= self.eqcounter),"0;JMP",
                              "(LT.XPOS.{eqcount})".format(eqcount= self.eqcounter),"@R13","D=M","@LT.XPOS.YNEG.{eqcount}".format(eqcount= self.eqcounter),"D;JLT","(LT.NO.OF.{eqcount})".format(eqcount= self.eqcounter),"@R13",
                              "D=M","@R14","D=D-M","@LT.FALSE.{eqcount}".format(eqcount= self.eqcounter),"D;JLE","@SP","A=M","M=-1","@LT.TRUE.{eqcount}".format(eqcount= self.eqcounter),
                              "0;JMP","(LT.FALSE.{eqcount})".format(eqcount= self.eqcounter),"@SP","A=M","M=0","(LT.TRUE.{eqcount})".format(eqcount= self.eqcounter),"@LT.END.{eqcount}".format(eqcount= self.eqcounter),"0;JMP",
                              "(LT.XPOS.YNEG.{eqcount})".format(eqcount= self.eqcounter),"@SP","A=M","M=0","@LT.END.{eqcount}".format(eqcount= self.eqcounter),"0;JMP","(LT.XNEG.YPOS.{eqcount})".format(eqcount= self.eqcounter),
                              "@SP","A=M","M=-1","(LT.END.{eqcount})".format(eqcount= self.eqcounter),"@SP","M=M+1"]
                self.eqcounter += 1
            case 6:
                asmstrlist = ['@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=M&D']
            case 7:
                asmstrlist = ['@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=M|D']
            case 8:
                asmstrlist = ['@SP', 'A=M-1',"M=!M"]
            case _:
                print("Can't match any ArithType")
        return asmstrlist

    def PushPopTemplate(self,number,variable,popOrpushType): #Todo
        asmstrlist = []
        if(variable):
            match popOrpushType:
                case 0:
                    asmstrlist = ['@ARG', 'D=M', '@' + str(number), 'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 1:
                    asmstrlist = ['@LCL', 'D=M', '@'+str(number), 'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 2:
                    asmstrlist = ['@StaticTest.{number}'.format(number=number), 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 3 :
                    asmstrlist = ["@"+str(number),"D=A","@SP","M=M+1","A=M-1","M=D"]  #Push Constant
                case 4:
                    asmstrlist = ['@THIS', 'D=M', '@'+str(number), 'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 5:
                    asmstrlist =['@THAT', 'D=M', '@'+str(number), 'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 6:
                    if(number == "0"):
                        asmstrlist = ['@THIS', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                    else:
                        asmstrlist = ['@THAT', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
                case 7:
                    asmstrlist = ['@5', 'D=A', '@'+str(number), 'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', '@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'M=M-1', 'A=M', 'M=D+M', '@SP', 'M=M+1']
                case _:
                    print("Can't match any PushType")
        else:
            match popOrpushType:
                case 0:
                    asmstrlist = ['@ARG', 'D=M', '@' + str(number), 'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 'A=M', 'M=D']
                case 1:
                    asmstrlist = ['@LCL', 'D=M', '@' + str(number), 'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 'A=M', 'M=D']
                case 2:
                    asmstrlist = ['@SP', 'AM=M-1', 'D=M', '@StaticTest.{number}'.format(number=number), 'M=D']
                case 3 :
                    asmstrlist = ["@"+str(number),"D=A","@SP","M=M-1","A=M+1","M=D"]  #Pop Constant
                case 4:
                    asmstrlist = ['@THIS', 'D=M', '@'+str(number), 'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 'A=M', 'M=D']
                case 5:
                    asmstrlist = ['@THAT', 'D=M', '@'+str(number), 'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 'A=M', 'M=D']
                case 6:
                    if(number == "0"):
                        asmstrlist = ['@SP', 'M=M-1', 'A=M', 'D=M', '@THIS', 'M=D']  #pointer has 0 and 1
                    else:
                        asmstrlist = ['@SP', 'M=M-1', 'A=M', 'D=M', '@THAT', 'M=D']
                case 7:
                    asmstrlist = ['@5', 'D=A', '@'+str(number), 'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 'A=M', 'M=D']
                case _:
                    print("Can't match any PopType")
        return asmstrlist
