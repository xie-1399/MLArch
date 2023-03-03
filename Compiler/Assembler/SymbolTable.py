
#标签符号和变量符号表,注意这里可能实现的方法是只要是符号就需要加进去
class SymbolTable(object):
    #Todo 可以考虑添加哈希表的结构
    def __init__(self,asmcodelists,TableList,getornot):
        self.TableList = TableList
        self.labelcount = 0
        #增加预先定义的符号表，标签对应的还需要看情况
        if(getornot):
            self.PredefineSym(getornot)
            self.Addlabelsignal(asmcodelists)
            self.AddVariablesignal(asmcodelists)

    def addEntry(self,sysmbol,address):
        self.TableList.update({str(sysmbol):address})  #符号表里添加元素,有相同的键会直接进行替换

    def contains(self,symbol):
        if (self.TableList.get(symbol)!= None):
            return True
        else:
            return False

    def getAddress(self,symbol):
        return self.TableList.get(symbol,-1) # No else return -1

    # 预定义好的符号
    def PredefineSym(self,getorNot):
        if (getorNot):
            print("PreDefine Symbols:")
            self.TableList.update({'SP': 0, "LCL": 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576})
            for i in range(0, 16):
                self.TableList.update({"R" + str(i): i})
                if (i == 15):
                    print("Add PreDefine Symbols Finish!")

    #变量映射
    def AddVariablesignal(self,asmcodelists):
        addresstart = 16
        for asmcode in asmcodelists:
            if(str(asmcode).startswith("@")):
                asmcode = str(asmcode).lstrip("@")
                if(not self.contains(asmcode) and not asmcode.isdigit()):  #这里也对预定义的一些符号进行了更新，去除了contains
                    self.addEntry(str(asmcode),addresstart)
                    addresstart = addresstart + 1

    #对应所加的地址应该根据程序的行数来进行加，要利用数字来记录
    def Addlabelsignal(self,asmcodelists):
        for asmcode in asmcodelists:
            if (str(asmcode).startswith("(")):
                asmcode = str(asmcode).lstrip("(").rstrip(")")
                if(not self.contains(asmcode)):
                    self.addEntry(asmcode,self.labelcount)
            else:
                self.labelcount +=1