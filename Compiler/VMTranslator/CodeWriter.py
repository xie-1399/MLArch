
#将对应的vm命令翻译成Hack汇编代码，需要写入对应的asm文件
#如果是push/pop一个数的流程 （1）把这个数先要存到对应的D寄存器里面去 （2）
class CodeWriter(object):

    def __init__(self,WriteFile,vmcodes):
        with open(WriteFile,"w+") as asmfile:
            for vmcode in vmcodes:

                asmfile.write()


    #算数操作对应的汇编代码
    def writeArithmetic(self,Command):
        pass

    #Just For Pop And Push
    def WritePushPop(self):
        pass