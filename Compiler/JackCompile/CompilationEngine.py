#将原有的字元列表加上对应的开始与终止符
class CompilationEngine(object):
    def __init__(self,tokenlist):
        self.tokenlist = tokenlist
        self.engine = []
        self.parameterlist = []
        compileclass = self.CompileClass()
        self.CompileClassVarDec(compileclass)
        self.CompileSubroutine(compileclass)

    def CompileClass(self):
        classCompile = False
        leftsig,rightsig= 0,0
        for tk in range(0,len(self.tokenlist)):
            if(self.tokenlist[tk].get("KEYWORD") == "class"):
                self.tokenlist.insert(tk,{"class":"start"})
                classCompile = True
            elif(self.tokenlist[tk].get("SYMBOL") == "{"):
                leftsig += 1
            elif(self.tokenlist[tk].get("SYMBOL") == "}"):
                rightsig += 1
            if(leftsig == rightsig and leftsig != 0):
                self.tokenlist.insert(tk + 1, {"class": "end"})
        if(classCompile):
            return True
        else:
            raise RuntimeError("No Class Find!")

    def CompileClassVarDec(self,compileclass):
        vardecone = False
        vardectwo = False
        if(compileclass):
            for tk in range(0, len(self.tokenlist)):
                if(self.tokenlist[tk].get("KEYWORD") == "class"):
                    vardecone = True
                if(vardecone and self.tokenlist[tk].get("SYMBOL") == "{"):
                    if(self.tokenlist[tk+1].get("KEYWORD") == "staic" or self.tokenlist[tk+1].get("KEYWORD") == "field"):
                        self.tokenlist.insert(tk + 1,{"classVarDec":"start"})
                        vardectwo = True
                if(vardectwo and self.tokenlist[tk].get("SYMBOL") == ";"):
                    self.tokenlist.insert(tk + 1, {"classVarDec": "end"})
                    vardectwo = False
                    break
        else:
            return None

    #contain the body
    def CompileSubroutine(self,compileclass):
        compilesub = False
        compilebody = False
        compileparameter = False
        if(compileclass):
            satisfify = ["function","method","constructor"]
            for tk in range(0, len(self.tokenlist)):
                if ((self.tokenlist[tk].get("KEYWORD")) in satisfify):
                    self.tokenlist.insert(tk,{"subroutineDec": "start"})
                    compilesub = True
                if(compilesub and self.tokenlist[tk].get("SYMBOL") == "("):
                    self.tokenlist.insert(tk+1,{"parameterList":"start"})
                    compileparameter = True
                    temp_tkpara = tk
                    while(self.tokenlist[temp_tkpara].get("SYMBOL") != ")"):
                        temp_tkpara += 1
                        self.parameterlist.append(self.tokenlist[temp_tkpara])
                    self.CompileParameterList(compileparameter,self.parameterlist)
                    self.tokenlist.insert(temp_tkpara, {"parameterList": "end"})


        else:
            return None

    def CompileParameterList(self,compileparameter,parameterlist):
        if(compileparameter):
            return parameterlist  #Todo can return the value
        else:
            return None

    def CompileVarDec(self):
        pass

    # Try to use the state machine
    def CompileStatements(self):
        pass

    def CompileDo(self):
        pass

    def CompileLet(self):
        pass

    def CompileWhile(self):
        pass

    def CompileReturn(self):
        pass

    def CompileIF(self):
        pass

    def CompileExpression(self):
        pass

    def CompileTerm(self):
        pass

    def CompileExpressionList(self):
        pass