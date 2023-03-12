
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
    "local":1,
    "static":2,
    "constant":3,
    "this":4,
    "that":5,
    "pointer":6,
    "temp":7
}


MemoryAccessCommands = ["pop","push"]
CommandTypes = {"C_ARITHMETIC":1,
    "C_LABEL":2,
    "C_GOTO":3,
    "C_IF":4,
    "C_POP":5,
    "C_PUSH":6,
    "C_FUNCTION":7,
    "C_RETURN":8,
    "C_CALL":9
}

