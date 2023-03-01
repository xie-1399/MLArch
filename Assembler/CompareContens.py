#比较与测试文件内容的差异
import operator
def ContentIsSame(sourcepath,testpath):
    try:
        with open(sourcepath,"r") as source, open(testpath,"r") as test:
            Sourcelines = source.readlines()
            testlines = test.readlines()
            if(operator.eq(Sourcelines,testlines)):  # Maybe use == also works
                return True
            else:
                return False

    except IOError as e:
        print("Can't find the file path")