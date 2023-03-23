#根据对应的语法规则将输入转化为对应的字元
class Tokenizer(object):
    def __init__(self,file):
        if(not str(file).endswith("jack")):
            raise RuntimeError("The file is not jackfile!")
        with open(file,"r") as jackfile:
            jacklines = jackfile.readlines()
            jacklines = self.clear(jacklines)

            jackfile.close()
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
                jackcodes.append(str(jackline))
        if "" in jackcodes:
            jackcodes.remove("")  #Todo
        return jackcodes

    def hasMoreTokens(self):
        pass

    def advance(self):
        pass

    def tokenType(self):
        pass

    def keyword(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
        pass



