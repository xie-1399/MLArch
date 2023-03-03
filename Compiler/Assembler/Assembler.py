#Assembler 编译器
from Compiler.Assembler.Code import Code
from Compiler.Assembler.CompareContens import ContentIsSame
from Compiler.Assembler.Parser import Parse
from Compiler.Assembler.SymbolTable import SymbolTable
from Compiler.Assembler.signalUntils import writeintofile


#dest = comp ; jump
if __name__ == '__main__':
     TestfileLists = ["Add","Pong","PongL","Rect","RectL"]
     for i in range(0,len(TestfileLists)):
          parse = Parse("./test/"+ TestfileLists[i] + ".asm",FirstRead=True,TableList={})
          #First Read Add sysmbol to table
          symboltables = SymbolTable(parse.asmvalidcodes,TableList={},getornot=True)


          #Second convert the signal
          # print(symboltables.TableList)
          parse = Parse("./test/"+ TestfileLists[i] + ".asm",FirstRead=False,TableList=symboltables.TableList)
          codebinlists = Code(parse.asmvalidcodelists).codebinlists
          writeintofile("./"+ TestfileLists[i] + ".ref", codebinlists)
          print(ContentIsSame("./test/"+ TestfileLists[i] + ".hack", "./"+ TestfileLists[i] + ".ref"))


#整体思路可能有一些地方不太一样，这个地址并不是按照对应的进行加一，而是根据程序本身对应的行数去选择把address加入进去












