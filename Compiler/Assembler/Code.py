#将对应的Hack语言的助记符转化为二进制码
from signalUntils import *
from Compiler.HackCompiler.Assembler.Parser import Parse
from CompareContens import *

class Code(object):
    def __init__(self,signallists):
        self.codebinlists = []
        for signallist in signallists:
            destbin = self.dest(signallist)
            compbin = self.comp(signallist)
            jumpbin = self.jump(signallist)
            if(signallist[2] == "A_COMMAND"):
                self.codebin = "0" + fillzero(str(signallist[3]),15)
            else:
                self.codebin = "111" + str(compbin) + str(destbin) + str(jumpbin)
            self.codebinlists.append(self.codebin)
    def dest(self,signallist):
        destsignal = signallist[-3]
        if(destsignal == None) :
            destsignal = ""
        return DEST.get(destsignal)
    def comp(self,signallist):
        compsignal = signallist[-2]
        if(compsignal == None):
            compsignal =""
        return Comps.get(compsignal)

    def jump(self,signallist):
        jumpsignal = signallist[-1]
        if(jumpsignal == None):
            jumpsignal = ""
        return JUMP.get(jumpsignal)

