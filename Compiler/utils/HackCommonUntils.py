# 比较与测试文件内容的差异,一些共有的类
import operator
import re


def ContentIsSame(sourcepath, testpath):
    try:
        with open(sourcepath, "r") as source, open(testpath, "r") as test:
            Sourcelines = source.readlines()
            testlines = test.readlines()
            Sourcelines = clearblank(Sourcelines)

            if(len(testlines) == 1):
                testlines = onelineabstract(testlines)
            else:
                testlines = clearblank(testlines)  # Not One line
            print(Sourcelines)
            print(testlines)
            if (operator.eq(Sourcelines, testlines)):  # Maybe use == also works
                return True
            else:
                for i in range(0, len(Sourcelines)):
                    if (Sourcelines[i] != testlines[i]):
                        print("Wrong Line is " + str(i + 1))
                        print("Sourcelines[i]:", Sourcelines[i])
                        print("testlines[i]:",testlines[i])
                        return False
            test.close()
    except IOError as e:
        print("Can't find the file path")

# 除去注释和空行对应的干扰，只比较对应的文件内容
def clearblank(linelists):
    newlinelists = []
    for linelist in linelists:
        if (str(linelist).startswith("//") or str(linelist) == "\n" or len(linelist) == 0):
            continue
        else:
            linelist = str(linelist).strip().replace(" ", "").rstrip("\n")
            newlinelists.append(linelist)
    return newlinelists


def onelineabstract(linelist):
    return re.findall(r'[\'](.*?)[\']',str(linelist))  #match the ''

#为了避免重复造轮子，这里还是定义一些方便抽取文本的函数
def getfileAritrhTemplate(file,content):
    strlist = []
    with open(file,"r") as filestrlist:
        filelines = filestrlist.readlines()
        stop = True
        for fileline in filelines:
            if(str(fileline).find(str(content))!=-1): #find will re
                stop = False
            elif(not stop):
                if(str(fileline)=="\n" or str(fileline)==""):
                    continue
                strlist.append(str(fileline).strip().rstrip("\n"))
                if(str(fileline).startswith("//")):
                     break
        strlist.pop(-1)
        return strlist

print(getfileAritrhTemplate("../VMTranslator/test/StackTest.asm", "//sub"))