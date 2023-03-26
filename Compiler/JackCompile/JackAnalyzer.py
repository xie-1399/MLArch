#关于Jack语言的词法分析器
from Compiler.JackCompile.JackTokenizer import Tokenizer
from Compiler.utils.HackCommonUntils import ContentIsSame
from SyntaxUntils import *
if __name__ == '__main__':

    filelist = ["./test/ArrayTest/Main.jack","./test/ExpressionLessSquare/Main.jack","./test/Square/Main.jack"]

    for file in filelist:
        tokensobject = Tokenizer(file)
        writeTxmlfile(tokensobject.tokens)
        #Compare file
        print(ContentIsSame(file.rstrip(".jack") + "T.xml","./testT.xml"))
