#关于Jack语言的词法分析器
from Compiler.JackCompile.CompileASTEngine import CompilationASTEngine
from Compiler.JackCompile.TokenAST import JackASTTokenizer
import typing

from Compiler.JackCompile.vm_writer import VMWriter


def compile_file(
        input_file:typing.TextIO, output_file: typing.TextIO):
    """Compiles a single file.

    Args:
        input_file (typing.TextIO): the file to compile.
        output_file (typing.TextIO): writes all output to this file.
    """
    # Your code goes here!
    # This function should be relatively similar to "analyze_file" in
    # JackAnalyzer.py from the previous project.
    tokenizer = JackASTTokenizer(input_file)
    vm_writer = VMWriter(output_file)
    engine = CompilationASTEngine(tokenizer, vm_writer)
    engine.compile_class()

# if __name__ == '__main__':
#
#     '''
#     : 存在的一些问题
#     （1）灵活性，部分代码过于冗余
#     （2）term、else、statements的处理不太相同
#     （3）异常处理机制不完善
#     （4）代码结构也不太清晰
#      (5) 嵌套的可能做不了
#     '''
#     '''
#     重构的几个目标：（1）清晰合理的接口设计  （2）数据结构  （3）异常处理
#     '''
#     filelist = ["./test/ArrayTest/Main.jack"]
#     compareToken = False
#     for file in filelist:
#         new_file = file.split("/")[-1].rstrip(".jack") + ".vm"
#         tokensobject = Tokenizer(file)
#         # print("before:",tokensobject.tokens)
#         # addanaly = CompilationEngine(tokensobject.tokens)
#         # print("after:",addanaly.tokenlist)
#
#         if(compareToken):
#             writeTxmlfile(tokensobject.tokens)
#         #Compare file
#             print(ContentIsSame(file.rstrip(".jack") + "T.xml","./testT.xml"))
#
#         else:
#             with open(file, 'r') as input_file, \
#                     open(new_file, 'w') as output_file:
#                 compile_file(input_file, output_file)
            # writexmlfile(addanaly.engine,showorwrite= False)
            # print(ContentIsSame(file.rstrip(".jack") + ".xml", "./test.xml"))

