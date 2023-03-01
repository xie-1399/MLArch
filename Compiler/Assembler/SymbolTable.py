class SymbolTable(object):
    def __init__(self):
        self.TableList = {}
        #增加预先定义的符号表，标签对应的还需要看情况
        self.PredefineSym(True)


    def addEntry(self,sysmbol,address):
        self.TableList.update({str(sysmbol):address})  #符号表里添加元素,有相同的键会直接进行替换

    def contains(self,symbol):
        if (self.TableList.get(symbol)!= None):
            return True
        else:
            return False

    def getAddress(self,symbol):
        return self.TableList.get(symbol,-1)

    # 预定义好的符号
    def PredefineSym(self,getorNot):
        if (getorNot):
            print("PreDefine Symbols:")
            self.TableList.update({'SP': 0, "LCL": 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576})
            for i in range(0, 16):
                self.TableList.update({"R" + str(i): i})
                if (i == 15):
                    print("Add PreDefine Symbols Finish!")

    #标签映射
    # def VariableAddress(Variable, AddressList, AddressStart):
    #     # 连续映射
    #     VariableOrNot = Variable in AddressList
    #     if (VariableOrNot):
    #         return AddressStart, AddressList, AddressList.get(Variable)
    #     else:
    #         AddressList.update({str(Variable): AddressStart + 1})
    #         return AddressStart + 1, AddressList, AddressStart + 1

#Just test
# symbols = SymbolTable()
# symbols.addEntry("go",11)
# print(symbols.contains("go"))
# print(symbols.getAddress("go"))
# print(symbols.TableList)