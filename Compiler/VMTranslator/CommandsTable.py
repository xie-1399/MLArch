
ArithmeticCommands = {"add":"M=D+M",
                      "sub":"M=M-D",
                      "neg":"",
                      "eq":"",
                      "gt":"",
                      "lt":"",
                      "and":"",
                      "or":"",
                      "not":""}

PointerType = {
    "0":"@THIS",
    "1":"@THAT",
}

ArithmeticType = {"add":0,
                  "sub":1,
                  "neg":2,
                  "eq":3,
                  "gt":4,
                  "lt":5,
                  "and":6,
                  "or":7,
                  "not":8}

memoryAccessType = {
    "argument":0,
    "loacl":1,
    "static":2,
    "constant":3,
    "this":4,
    "that":5,
    "pointer":6,
    "temp":7
}


MemoryAccessCommands = ["pop","push"]

