#关于Jack语言的词法分析器
from Compiler.JackCompile.JackTokenizer import Tokenizer
from Compiler.utils.HackCommonUntils import ContentIsSame
from SyntaxUntils import *
from CompilationEngine import *
if __name__ == '__main__':

    '''
    : 存在的一些问题
    （1）灵活性，部分代码过于冗余
    （2）term、else、statements的处理不太相同
    （3）异常处理机制不完善
    （4）代码结构也不太清晰
     (5) 嵌套的可能做不了
    '''
    '''
    重构的几个目标：（1）清晰合理的接口设计  （2）数据结构  （3）异常处理
    '''

    filelist = ["./test/ArrayTest/Main.jack"]
    compareToken = False
    for file in filelist:
        tokensobject = Tokenizer(file)
        # print("before:",tokensobject.tokens)
        addanaly = CompilationEngine(tokensobject.tokens)
        # print("after:",addanaly.tokenlist)

        if(compareToken):
            writeTxmlfile(tokensobject.tokens)
        #Compare file
            print(ContentIsSame(file.rstrip(".jack") + "T.xml","./testT.xml"))

        else:
            writexmlfile(addanaly.engine,showorwrite= False)
            print(ContentIsSame(file.rstrip(".jack") + ".xml", "./test.xml"))