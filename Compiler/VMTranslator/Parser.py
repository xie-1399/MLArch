
#Version  1
#1:Memory Access Commands 2:Arithmetic and Logical Commands
class Parser(object):
    def __init__(self,File):
        try:
            self.vmcodeList = []
            if(not str(File).endswith("vm")):
                print("The Parse File is not vm file")
                return
            with open(File,"r") as Vmfile:
                self.vmlines = Vmfile.readlines()
                self.vmcodes = self.clear(self.vmlines)
                self.clearvmcodes = self.clear(self.vmlines)
                for i in range(0,len(self.vmcodes)):
                    self.vmcodeList.append(self.Process(self.vmcodes))
                    self.vmcodes.pop(0)
                Vmfile.close()

        except IOError as e:
            print("The file is not exit!")

    def Process(self,vmcodes):
        hasMoreCommands = self.hasMoreCommands(vmcodes)
        advance = self.advance(hasMoreCommands,vmcodes)
        commandType = self.commandType(advance)
        Arg1 = self.Arg1(advance,commandType)
        Arg2 = self.Arg2(advance,commandType)
        return hasMoreCommands,advance,commandType,Arg1,Arg2

    def clear(self,vmlines):
        vmcodes = []
        for vmline in vmlines:
            if(str(vmline).startswith("//") or str(vmline) == "\n"):
                continue
            else:
                vmline = vmline.rstrip("\n").lstrip()
                #vmline = vmline.replace(" ","") #中间的空格暂时不用去除
                vmcodes.append(str(vmline))
        return vmcodes

    def hasMoreCommands(self,vmcodes):
        if(len(vmcodes) > 0):
            return True
        else:
            return False

    def advance(self,hasMoreCommand,vmcodes):
        if (hasMoreCommand):
            advance = vmcodes[0]
            return advance
        else:
            print("Advance Command is None")

    def commandType(self,vmcode):  #Todo
        #v1暂时只考虑计算和访存两种类型
        if(str(vmcode).startswith("pop")):
            return "C_POP"
        elif(str(vmcode).startswith("push")):
            return "C_PUSH"
        else:
            return "C_ARITHMETIC"


    #返回当前命令的第一个参数
    def Arg1(self,vmcode,Commandtype): #Todo
        if(Commandtype == "C_ARITHMETIC"):
            return vmcode
        else:
             return str(vmcode).split(" ")[1]

    def Arg2(self,vmcode,Commandtype):
        if(Commandtype == "C_PUSH" or Commandtype == "C_POP"):
            return str(vmcode).split(" ")[2]
        else:
            return None