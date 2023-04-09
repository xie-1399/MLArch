'''
:能够完成一个完整的编译的流程，能够从前端（Jack） -> vm -> asm -> binary
:后续可以考虑改成使用命令行的形式，暂时先完成一键编译
'''
import argparse
from JackCompile import JackAnalyzer
from VMTranslator import Translator
from Assembler import Assembler
if __name__ == '__main__':
    sourcefile = "./Main.jack"
    newfile = "./Main.vm"
    asmfile = "./Main.asm"
    hackfile = "./Main.hack"
    with open(sourcefile, 'r') as input_file, open(newfile, 'w') as output_file:

        JackAnalyzer.compile_file(input_file = input_file , output_file = output_file)  #convert to the vmfile

        input_file.close()
        output_file.close()

    Translator.compileVm(newfile,asmfile)  #vm to asm

    Assembler.compileAssembler(asmfile,hackfile) #asm to jack
