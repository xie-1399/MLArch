#关于Jack语言的词法分析器
from Compiler.JackCompile.JackTokenizer import Tokenizer
from Compiler.utils.HackCommonUntils import ContentIsSame
from SyntaxUntils import *
from CompilationEngine import *
if __name__ == '__main__':

    filelist = ["./test/ArrayTest/Main.jack","./test/ExpressionLessSquare/Main.jack","./test/Square/Main.jack"]
    compareToken = False
    for file in filelist:
        tokensobject = Tokenizer(file)
        print("before:",tokensobject.tokens)
        addanaly = CompilationEngine(tokensobject.tokens)
        print("after:",addanaly.tokenlist)

        if(compareToken):
            writeTxmlfile(tokensobject.tokens)
        #Compare file
            print(ContentIsSame(file.rstrip(".jack") + "T.xml","./testT.xml"))


