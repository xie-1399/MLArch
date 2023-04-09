#词法分析的一些工具类
import re
from collections import deque

KeyWords = [
    "CLASS",
    "DO",
    "IF",
    "ELSE",
    "WHILE",
    "RETURN",
    "FUNCTION",
    "CONSTRUCTOR",
    "INT",
    "BOOLEAN",
    "CHAR",
    "METHOD",
    "VOID",
    "VAR",
    "STATIC",
    "FIELD",
    "LET",
    "TRUE",
    "FALSE",
    "NULL",
    "THIS"
]

#Stop siganl
keyword_c = re.compile("^\s*(false|do|if|null|this|let|else|while|return|static|field|var|int|char|boolean|void|true|class|method|constructor|function)\s*")
identifier_c = re.compile("^\s*([a-zA-Z_][a-zA-Z_1-9]*)\s*")  #注意\s会匹配对应的空白
integerconstant_c = re.compile("^\s*(\d+)\s*") #Todo <32767
stringconstant_c = re.compile("^\s*\"(.*)\"\s*") #\"
symbol_c = re.compile("^\s*([{}()\[\].,;+\-*/&|~>=<])\s*") #\[ \]
StopSignals = [keyword_c,identifier_c,integerconstant_c,stringconstant_c,symbol_c]

tokenType = {
    1:"KEYWORD",2:"IDENTIFIER",
    3:"INT-CONST",4:"STRING_COUNT",5:"SYMBOL",
}

KeepSignal = ["class","classVarDec","subroutineDec","parameterList","subroutineBody","varDec"
              ,"statements","whileStatement","ifStatement","returnStatement","letStatement"
              ,"doStatement","expression","term","expressionlist"]

#自定义spilt Todo a little slow
def my_spilt(string,regex):
    spiltlist = []
    Flag = False
    tempstr = ""
    for i in range(0,len(string)):
        if(string[i] == "\""):
            Flag = not Flag
        if(Flag):
            tempstr += string[i]
            continue
        if(string[i] == regex):
            if(not tempstr):
                continue
            spiltlist.append(tempstr)
            tempstr = ""
        else:
            tempstr += string[i]
            if(i == len(string) - 1):
                spiltlist.append(tempstr)
    return spiltlist

def writeTxmlfile(tokens):
    type = {"KEYWORD":"keyword","IDENTIFIER":"identifier","INT-CONST":"integerConstant","STRING_COUNT":"stringConstant","SYMBOL":"symbol"}
    with open("./testT.xml","w+") as xmlfile:
        xmlfile.write("<tokens>\n")
        for tk in tokens:
            for tk_key,tk_value in tk.items():
                line = "<" + type.get(tk_key) + ">" + " " + tk_value.replace("\"","") + " " + "</" + type.get(tk_key) + ">" + "\n"
                xmlfile.write(line)
        xmlfile.write("</tokens>\n")
        xmlfile.close()

def writexmlfile(tokens,showorwrite):
    type = {"KEYWORD": "keyword", "IDENTIFIER": "identifier", "INT-CONST": "integerConstant",
            "STRING_COUNT": "stringConstant", "SYMBOL": "symbol"}
    with open("./test.xml","w+") as xmlfile:
        for index , tk in enumerate(tokens,1):
            for tk_key,tk_value in tk.items():
                if(tk_key == "start"):
                    line = "<" + tk_value + ">" + "\n"
                elif(tk_key == "end"):
                    line = "<" + "/" + tk_value + ">" + "\n"
                else:
                    line = "<" + type.get(tk_key) + ">" + " " + tk_value.replace("\"", "") + " " + "</" + type.get(tk_key) + ">" + "\n"
                if(not showorwrite):
                    xmlfile.write(line)
                else:
                    print("{index} : {line}".format(index = index,line = line))
        xmlfile.close()

def expressionutil(finish,expressionlist,statetoken,addlist):
    if(addlist):
        if(finish):
            expressionlist.append({"end": "term"})
            expressionlist.append({"end": "expression"})
            expressionlist.append({"end": "expressionList"})
            expressionlist.append(statetoken)
        else:
            expressionlist.append(statetoken)
            expressionlist.append({"start": "expressionList"})
            expressionlist.append({"start": "expression"})
            expressionlist.append({"start": "term"})

    else:
        if(finish):
            expressionlist.append({"end": "term"})
            expressionlist.append({"end": "expression"})
            expressionlist.append(statetoken)
        else:
            expressionlist.append(statetoken)
            expressionlist.append({"start": "expression"})
            expressionlist.append({"start": "term"})

