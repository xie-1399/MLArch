#将原有的字元列表加上对应的开始与终止符
from Compiler.JackCompile.SyntaxUntils import writexmlfile
from StateMachine import *
class CompilationEngine(object):
    def __init__(self,tokenlist):
        self.tokenlist = tokenlist
        self.engine = []
        self.parameterlist = []
        self.funcnum = self.functionnum(tokenlist)
        compileclass = self.CompileClass()
        self.CompileClassVarDec(compileclass)
        self.CompileSubroutine(compileclass)

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
        compilestatement = []
        if(compileclass):
            satisfify = ["function","method","constructor"]
            tk, token_length = 0, len(self.tokenlist)
            while(tk < token_length):
                if ((self.tokenlist[tk].get("KEYWORD")) in satisfify):
                    self.tokenlist.insert(tk,{"start":"subroutineDec" })
                    tk += 1
                    token_length += 1
                    compilesub = True

                if(compilesub and self.tokenlist[tk].get("SYMBOL") == "("):
                    self.tokenlist.insert(tk+1,{"start":"parameterList"})
                    tk += 1
                    token_length += 1
                    compileparameter = True
                    temp_tkpara = tk
                    while(self.tokenlist[temp_tkpara].get("SYMBOL") != ")"):
                        temp_tkpara += 1
                        self.parameterlist.append(self.tokenlist[temp_tkpara])
                    self.CompileParameterList(compileparameter,self.parameterlist)
                    self.tokenlist.insert(temp_tkpara, {"end":"parameterList" })
                    tk += 1
                    token_length += 1

                if (compilesub and self.tokenlist[tk].get("SYMBOL") == "{"):
                    self.tokenlist.insert(tk, {"start":"subroutineBody" })
                    tk += 1
                    token_length += 1

                    temp_tkbody = tk
                    while(self.tokenlist[temp_tkbody].get("SYMBOL") != "}"):
                        temp_tkbody += 1
                        compilebody.append(self.tokenlist[temp_tkbody])
                    statementstart = self.CompileVarDec(tk + 1,len(compilebody))
                    compilerbodylist = self.CompileBodyList(compilebody)

                    statetemp = statementstart
                    while(self.tokenlist[statementstart].get("KEYWORD") != "return"):
                        compilestatement.append(self.tokenlist[statementstart])
                        statementstart += 1
                    compilestatement.append(self.tokenlist[statementstart])
                    compilestatement.append(self.tokenlist[statementstart + 1])
                    # print("CompileStatement:",compilestatement)

                    compilestatementlist = self.CompileStatementList(compilestatement)
                    #Machine Conver
                    Statementmachine = Statement(compilestatement,statetemp,statementstart + 1) #contains before and after
                    expression = Statementmachine.expression
                    # writexmlfile(Statementmachine.expression,True)
                    beforecom = self.tokenlist[0:statetemp]

                    if(self.funcnum == 1):
                        aftercoms = self.tokenlist[statementstart + 2:]
                    else:
                        aftercoms = self.tokenlist[statementstart + 2 : statementstart + 3]
                        print(aftercoms)
                    aftercomchange = []
                    bodycount = 0
                    for index,aftercom in enumerate(aftercoms):
                        if(aftercom.get("SYMBOL") == '}' and bodycount == 0):
                            aftercomchange.append(aftercom)
                            aftercomchange.append({"end":"subroutineBody"})
                            bodycount = bodycount + 1
                        elif(aftercom.get("SYMBOL") == '}' and bodycount == 1):
                            aftercomchange.append({"end": "subroutineDec"})
                            aftercomchange.append(aftercom)
                        else:
                            aftercomchange.append(aftercom)
                    self.tokenlist = beforecom + expression + aftercomchange

                    compilebody.clear()  #每个body单独分开
                    compilestatement.clear()
                    compilesub = False
                    tk += 1
                    token_length += 1
                tk += 1
        else:
            return None

    def CompileParameterList(self,compileparameter,parameterlist):
        if(compileparameter):
            return parameterlist  #Todo can return the value
        else:
            return None

    def CompileBodyList(self, compilebody):
            return compilebody  # Todo can return the value

    def CompileStatementList(self, compilestatement):
            return compilestatement  # Todo can return the value

    def CompileVarDec(self,bodystart,bodyend):
        statements = ["let","if","else","while","do","return"]
        tk, token_length = bodystart, bodyend
        while (tk < token_length):
        #for index , bodysig in enumerate(compilebody,1):
            if(self.tokenlist[tk].get("KEYWORD") == "var"):
                self.tokenlist.insert(tk, {"start": "varDec"}) #Todo
                tk += 1
                token_length += 1
            elif(self.tokenlist[tk].get("SYMBOL") == ";"):
                self.tokenlist.insert( tk + 1, {"end":"varDec"})
                tk += 1
                token_length += 1
            if(self.tokenlist[tk].get("KEYWORD") in statements):
                break
            tk =tk + 1
        return tk

    def functionnum(self,tokenlist):
        number = 0
        for token in tokenlist:
            if(token.get("KEYWORD") == "function"):
                number = number + 1
        return number








