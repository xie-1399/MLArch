#FSM状态机的结构
from collections import deque

from transitions import Machine

from Compiler.JackCompile.SyntaxUntils import expressionutil


# Try to use the state machine , and just about the statement
# if and while may contain other statement
class Statement(object):
    '''


    : 使用的列表的append操作过多
    : Statements只放在开头以及结尾即可
    '''
    def __init__(self, tokens, begin, end):

        self.tokens = tokens
        self.statetokens = []
        self.expresstion = []
        self.stack = deque()
        self.begin = begin
        self.end = end
        self.beginstatement = True
        self.start()
        self.stop()

    def start(self):
        state_ = 0
        letstate = letStatement()
        ifstate = ifStatement()
        whilestate = whileStatement()
        dostate = doStatement()
        returnstate = returnStatement()
        statelist = [letstate,ifstate,whilestate,dostate,returnstate]
        print("The StateMachine start!") # Todo
        self.statetokens.append({"start": "statements"})
        for index, token in enumerate(self.tokens):
            temp = state_
            if (token.get("KEYWORD") == "let"):
                state_ = 0
            elif (token.get("KEYWORD") == "if"):
                state_ = 1
            elif (token.get("KEYWORD") == "else"):
                state_ = 1
            elif (token.get("KEYWORD") == "while"):
                state_ = 2
            elif (token.get("KEYWORD") == "do"):
                state_ = 3
            elif (token.get("KEYWORD") == "return"):
                state_ = 4
            # elif (token.get("SYMBOL") == "{" and len(self.stack) == 0):
            #     self.statetokens.append({"start": "statements"})
            # elif (token.get("SYMBOL") == "}" and len(self.stack) == 0 ):
            #     self.statetokens.append({"end": "statements"})
            elif (token.get("SYMBOL") == "}" and len(self.stack) != 0):
                endsignal = self.stack.pop()
                self.statetokens.extend(statelist[temp].statetokens)
                statelist[temp].statetokens.clear()
                if(endsignal) == "ifend":
                    self.statetokens.append({"end": "ifStatement"})
                elif(endsignal) == "whileend":
                    self.statetokens.append(token)
                    self.statetokens.append({"end": "whileStatement"})
                    continue
            # print(statelist[state_].state)
            if temp != state_:
                self.statetokens.extend(statelist[temp].statetokens)
                statelist[temp].statetokens.clear()
            if(state_ == 1 or state_ == 2):
                statelist[state_].action(token, self.stack)
            # elif(state_ == 4):
            #     statelist[state_].action(token)
            #     self.statetokens.extend(statelist[state_].statetokens)
            else:
                statelist[state_].action(token)
        self.statetokens.extend(statelist[state_].statetokens)
        self.expression = Expressiontoken(self.statetokens)

    def stop(self):
        print("The StateMachine stop!")


class letStatement(object):
    def __init__(self):
        self.state = 'letStatement'
        self.statetokens = []

    def action(self,lettokens):
        if (lettokens.get("KEYWORD") == "let"):
            self.statetokens.append({"start": "letStatement"})
            self.statetokens.append(lettokens)
        elif (lettokens.get("SYMBOL") == ";"):
            self.statetokens.append(lettokens)
            self.statetokens.append({"end": "letStatement"})
        else:
            self.statetokens.append(lettokens)


class ifStatement(object):  # A little difference
    def __init__(self):
        self.state = 'ifStatement'
        self.statetokens = []
        self.elsetoken = False

    def action(self, iftokens,stack):
        if (iftokens.get("KEYWORD") == "if"):
            self.statetokens.append({"start": "ifStatement"})
            self.statetokens.append(iftokens)
        elif (iftokens.get("KEYWORD") == "else"):
            self.elsetoken = True
            self.statetokens.append({"start": "elseStatement"})
            self.statetokens.append(iftokens)
        elif(iftokens.get("KEYWORD") == "{"):
            stack.append("ifend")
        elif (iftokens.get("SYMBOL") == "}" and not self.elsetoken):
            self.statetokens.append(iftokens)
            self.statetokens.append({"end": "ifStatement"})
        elif (iftokens.get("SYMBOL") == "}" and self.elsetoken):
            self.statetokens.append(iftokens)
            self.statetokens.append({"end": "elseStatement"})
        else:
            self.statetokens.append(iftokens)


#use stack to add end while
class whileStatement(object):
    def __init__(self):
        self.state = 'whileStatement'
        self.statetokens = []

    def action(self, whiletokens,stack):
        if (whiletokens.get("KEYWORD") == "while"):
            self.statetokens.append({"start": "whileStatement"})
            self.statetokens.append(whiletokens)
        elif(whiletokens.get("SYMBOL") == "{"):
            self.statetokens.append(whiletokens)
            stack.append("whileend")
        elif(whiletokens.get("SYMBOL") == "("):

            self.statetokens.append(whiletokens)
            stack.append("whileend")
        else:
            self.statetokens.append(whiletokens)


class doStatement(object):
    def __init__(self):
        self.state = 'doStatement'
        self.statetokens = []

    def action(self, dotokens):
        if (dotokens.get("KEYWORD") == "do"):
            self.statetokens.append({"start": "doStatement"})
            self.statetokens.append(dotokens)
        elif (dotokens.get("SYMBOL") == ";"):
            self.statetokens.append(dotokens)
            self.statetokens.append({"end": "doStatement"})
        else:
            self.statetokens.append(dotokens)


class returnStatement(object):  # Todo
    def __init__(self):
        self.state = 'returnStatement'
        self.statetokens = []

    def action(self, returntokens):
        if (returntokens.get("KEYWORD") == "return"):
            self.statetokens.append({"start": "returnStatement"})
            self.statetokens.append(returntokens)
        elif (returntokens.get("SYMBOL") == ";"):
            self.statetokens.append(returntokens)
            self.statetokens.append({"end": "returnStatement"})
            self.statetokens.append({"end": "statements"})
        else:
            self.statetokens.append(returntokens)

#Todo function
def Expressiontoken(statetokens):
    expressionlist = []
    tk, token_length = 0, len(statetokens)
    while (tk < token_length):
        if(statetokens[tk].get("start") == "letStatement"):
            while(statetokens[tk].get("end") != "letStatement"):
                expresslet(statetokens[tk],expressionlist)
                tk = tk + 1
        if(statetokens[tk].get("start") == "doStatement"):
            while(statetokens[tk].get("end") != "doStatement"):
                if (statetokens[tk].get("SYMBOL") == "(" and statetokens[tk + 1].get("SYMBOL") == ")"):
                    expressionlist.append(statetokens[tk])
                    expressionlist.append({"start": "expressionList"})
                    expressionlist.append({"end": "expressionList"})
                    expressionlist.append(statetokens[tk + 1])
                    tk = tk + 1
                else:
                    expressDo(statetokens[tk],expressionlist)
                tk = tk + 1
        if(statetokens[tk].get("start") == "ifStatement"):
            flag = False
            while(statetokens[tk].get("end") != "ifStatement"):
                if(flag):
                    expressionlist.append(statetokens[tk])
                else:
                    if(statetokens[tk].get("SYMBOL") == "(" and statetokens[tk + 1].get("SYMBOL") != ")"):
                        expressionutil(False, expressionlist, statetokens[tk], True)
                    elif(statetokens[tk].get("SYMBOL") == "(" and statetokens[tk + 1].get("SYMBOL") == ")"):
                        expressionlist.append(statetokens[tk])
                        expressionlist.append({"start": "expressionList"})
                        expressionlist.append({"end": "expressionList"})
                        expressionlist.append(statetokens[tk+1])
                        tk = tk + 1
                    elif (statetokens[tk].get("SYMBOL") == ")"):
                        expressionutil(True, expressionlist, statetokens[tk], True)
                    elif (statetokens[tk].get("SYMBOL") == "{"):
                        flag = True
                    else:
                        expressionlist.append(statetokens[tk])
                tk = tk + 1
        if(statetokens[tk].get("start") == "whileStatement"):
            flag = False
            while(statetokens[tk].get("end") != "whileStatement"):
                if(statetokens[tk].get("start") == "letStatement"):
                    while (statetokens[tk].get("end") != "letStatement"):
                        expresslet(statetokens[tk], expressionlist)
                        tk = tk + 1
                    continue
                if(statetokens[tk].get("start") == "doStatement"):
                    while (statetokens[tk].get("end") != "doStatement"):
                        expressDo(statetokens[tk], expressionlist)
                        tk = tk + 1
                    continue
                if(flag):
                    expressionlist.append(statetokens[tk])

                else:
                    if(statetokens[tk].get("SYMBOL") == "("):
                        expressionutil(False, expressionlist, statetokens[tk], False)
                    elif (statetokens[tk].get("SYMBOL") == ")"):
                        expressionutil(True, expressionlist, statetokens[tk], False)
                    elif (statetokens[tk].get("SYMBOL") == "{"):
                        flag = True
                        expressionlist.append(statetokens[tk])
                    else:
                        expressionlist.append(statetokens[tk])
                tk = tk + 1
        expressionlist.append(statetokens[tk])
        tk = tk + 1
    return expressionlist

def expresslet(statetoken,expressionlist):
    if (statetoken.get("SYMBOL") == "["):
        expressionutil(False, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "]"):
        expressionutil(True, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "="):
        expressionutil(False, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == ";"):
        expressionutil(True, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "("):
        expressionutil(False, expressionlist, statetoken, True)
    elif (statetoken.get("SYMBOL") == ")"):
        expressionutil(True, expressionlist, statetoken, True)
    else:
        expressionlist.append(statetoken)
def expressDo(statetoken,expressionlist):
    if (statetoken.get("SYMBOL") == "["):
        expressionutil(False, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "]"):
        expressionutil(True, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "="):
        expressionutil(False, expressionlist, statetoken, False)
    elif (statetoken.get("SYMBOL") == "("):
        expressionutil(False, expressionlist, statetoken, True)
    elif (statetoken.get("SYMBOL") == ")"):
        expressionutil(True, expressionlist, statetoken, True)
    else:
        expressionlist.append(statetoken)
#Maybe one more pass ( but is really slow)
class Expression(object):  # Todo for the sub call

    def __init__(self,expression):
        self.oplist = ['+','-','*','/','&','|','<','>','=']
        self.unaryOp = ['~','-']
        self.KeywordConstant = ['true','false','null','this']
        self.op = expression
        self.startexpression()

    def startexpression(self):
        pass


    def startterm(self):
        pass

    def endterm(self):
        pass

    def startexpressionlist(self):
        pass

    def endexpressionlist(self):
        pass

    def endexpression(self):
        pass


#if want to use the libary
'''
class Matter(object):
    pass
model = Matter()
# 状态定义
states=['solid', 'liquid', 'gas', 'plasma']
# 定义状态转移
# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}]
# 初始化
machine = Machine(model=model, states=states, transitions=transitions, initial='solid')
# Test
print(model.state)   # solid
# 状体转变
model.melt()
print(model.state)   # liquid
'''
