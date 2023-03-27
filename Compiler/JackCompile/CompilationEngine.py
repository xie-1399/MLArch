#将原有的字元列表加上对应的开始与终止符
class CompilationEngine(object):
    def __init__(self,tokenlist):
        self.tokenlist = tokenlist
        self.engine = []
        self.parameterlist = []
        compileclass = self.CompileClass()
        self.CompileClassVarDec(compileclass)
        # self.CompileSubroutine(compileclass)

    def CompileClass(self):  #这里涉及一个问题就是拷贝与深拷贝的问题，一定需要注意
        classCompile = False
        leftsig,rightsig = 0,0
        tk,token_length = 0,len(self.tokenlist)
        while(tk < token_length):
            if(self.tokenlist[tk].get("KEYWORD") == "class" and not classCompile):
                self.tokenlist.insert(tk,{"start":"class"})
                token_length += 1
                tk += 1
                classCompile = True
            if(self.tokenlist[tk].get("SYMBOL") == "}"):
                rightsig += 1
            elif(self.tokenlist[tk].get("SYMBOL") == "{"):
                leftsig += 1
            if(leftsig == rightsig and leftsig != 0):
                self.tokenlist.insert(tk + 1, {"end":"class"}) #Todo for just one class
                token_length += 1
                tk += 1
            tk = tk + 1
        #print(f"leftsig:{leftsig},rightsig:{rightsig}".format(leftsig = leftsig , rightsig = rightsig))
        if(classCompile):
            return True
        else:
            raise RuntimeError("No Class Find!")

    def CompileClassVarDec(self,compileclass):
        vardecone = False
        vardectwo = False
        tk, token_length = 0, len(self.tokenlist)
        if(compileclass):
            while(tk < token_length):
                if(self.tokenlist[tk].get("KEYWORD") == "class"):
                    vardecone = True
                if(vardecone and self.tokenlist[tk].get("SYMBOL") == "{"):
                    if(self.tokenlist[tk+1].get("KEYWORD") == "static" or self.tokenlist[tk+1].get("KEYWORD") == "field"):
                        self.tokenlist.insert(tk + 1,{"start":"classVarDec"})
                        tk = tk + 1
                        token_length += 1
                        vardectwo = True
                if(vardectwo and self.tokenlist[tk].get("SYMBOL") == ";"):
                    self.tokenlist.insert(tk + 1, {"end":"classVarDec"})
                    vardectwo = False
                    tk = tk + 1
                    token_length += 1
                    break
                tk += 1
        else:
            return None

    #contain the body
    def CompileSubroutine(self,compileclass):
        compilesub = False
        compilebody = []
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
                if (compilesub and self.tokenlist[tk].get("SYMBOL") == "{"):
                    self.tokenlist.insert(tk, {"subroutineBody": "start"})
                    temp_tkbody = tk
                    while(self.tokenlist[temp_tkbody].get("SYMBOL") != "}"):
                        temp_tkbody += 1
                        compilebody.append(self.tokenlist[temp_tkbody])
                    self.CompileVarDec(compilebody,tk)
                    self.CompileStatements(compilebody,tk)
                    self.tokenlist.insert(temp_tkbody + 1, {"subroutineBody": "end"})
        else:
            return None

    def CompileParameterList(self,compileparameter,parameterlist):
        if(compileparameter):
            return parameterlist  #Todo can return the value
        else:
            return None

    def CompileVarDec(self,compilebody,bodystart):
        statements = ["let","if","else","while","do","return"]
        varfirst = True
        for index , bodysig in enumerate(compilebody,1):
            if(bodysig.get("KEYWORD") == "var" and varfirst):
                self.tokenlist.insert(bodystart + index, {"varDec": "start"}) #Todo
                varfirst = False
            elif(bodysig.get("KEYWORD") in statements):
                self.tokenlist.insert(bodystart + index, {"varDec": "end"})

    # Try to use the state machine
    def CompileStatements(self,compilebody,bodystart):
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