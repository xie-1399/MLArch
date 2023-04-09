#根据对应的语法规则将输入转化为对应的字元
from SyntaxUntils import *
class Tokenizer(object):
    def __init__(self,file):
        self.tokens = []
        self.value = []
        if(not str(file).endswith("jack")):
            raise RuntimeError("The file is not jackfile!")
        with open(file,"r") as jackfile:
            jacklines = jackfile.readlines()
            self.jacklines = self.clear(jacklines)
            jacklength = len(self.jacklines)
            for i in range(0,jacklength):
                #第一个词就表示了对应的句子类型,需要进行处理
                self.tokens.extend(self.Process(self.jacklines[0]))
                self.jacklines.pop(0)
            #print(self.tokens)
            jackfile.close()

    def Process(self,jackline):
        HasMoreTokens = self.hasMoreTokens()
        advance = self.advance(HasMoreTokens,jackline)
        tokentypelist = self.tokenType(advance)
        for tp in tokentypelist:
            if(tp.get('KEYWORD',-1) != -1):
                value = self.keyword(tp)
            elif(tp.get('IDENTIFIER',-1) != -1):
                value = self.identifier(tp)
            elif(tp.get('SYMBOL',-1) != -1):
                value = self.symbol(tp)
            elif (tp.get('INT-CONST', -1) != -1):
                value = self.intVal(tp)
            elif (tp.get('STRING_COUNT', -1) != -1):
                value = self.stringVal(tp)
            else:
                raise RuntimeError("No token value")
            self.value.append(value)
        return tokentypelist

    def clear(self,jacklines):
        jackcodes = []
        for jackline in jacklines:
            #注意内部的注释也是需要去清除的
            if(str(jackline).startswith("//") or str(jackline).startswith("/*") or str(jackline) == "\n"):
                continue
            else:
                jackline = jackline.rstrip("\n").strip().replace("\t","")
                if(jackline.find("//"))!=-1:
                    jackline = jackline.split("//")[0]
                if(not jackline):   #去除文件中的空行
                    continue
                jackcodes.append(str(jackline))
        return jackcodes

    def hasMoreTokens(self):
        if(len(self.jacklines) > 0) :
            return True
        else:
            return False

    def advance(self,HasMoreTokens,jackline):
        if(HasMoreTokens):
            return jackline
        else:
            raise RuntimeError("No Advance Tokens")

    #先考虑使用split进行分割
    def tokenType(self,advance):
        tokens = my_spilt(advance," ") #Todo about string constant
        tokenTypelist = []
        for token in tokens:
            while(len(token) != 0):
                for index , StopSignal in enumerate(StopSignals,1):
                    x = StopSignal.match(token)
                    if(x != None):
                        tokentype = tokenType.get(index)
                        constant = x.group()
                        token = token.strip(constant) #Todo
                        tokenTypelist.append({tokentype:constant})
                    else:
                        continue
        return tokenTypelist

    def keyword(self,tp):
        return tp.get("KEYWORD")

    def symbol(self,tp):
        return tp.get("SYMBOL")

    def identifier(self,tp):
        return tp.get("IDENTIFIER")

    def intVal(self,tp):
        return tp.get("INT-CONST")

    def stringVal(self,tp):
        return tp.get("STRING_COUNT")



