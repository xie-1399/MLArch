#Assembler 编译器
from Compiler.HackCompiler.Assembler.Code import Code
from Compiler.HackCompiler.Assembler.CompareContens import ContentIsSame
from Compiler.HackCompiler.Assembler.Parser import Parse
from Compiler.HackCompiler.Assembler.signalUntils import writeintofile

if __name__ == '__main__':
     parse = Parse("./test/Add.asm")
     codebinlists = Code(parse.asmvalidcodelists).codebinlists
     writeintofile("andv1.asm", codebinlists)
     print(ContentIsSame("./test/Add.hack", "./andv1.asm"))
    # PredefineSymbols = PredefineSym(True)
    # print(PredefineSymbols)
    # AddressStart = 15
    # print(VariableAddress("yes",PredefineSymbols,AddressStart))
    # print(VariableAddress("No",PredefineSymbols,AddressStart+1))\
    #Parse = Parse("test/Add.asm")















