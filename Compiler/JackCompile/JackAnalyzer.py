#关于Jack语言的词法分析器
from Compiler.JackCompile.JackTokenizer import Tokenizer

if __name__ == '__main__':

    filelist = ["./test/ArrayTest/Main.jack"]

    for file in filelist:
        Tokenizer(file)
