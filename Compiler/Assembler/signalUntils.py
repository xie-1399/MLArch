#对应的二进制表

Comps = {
    "": "0000000",
    "null": "0000000",
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
    "D>>": "0010000",
    "D<<": "0110000",
    "A>>": "0000000",
    "A<<": "0100000",
    "M>>": "1000000",
    "M<<": "1100000",
}

DEST = {
    "": "000",
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "DM": "011",
    "A": "100",
    "AM": "101",
    "MA": "101",
    "AD": "110",
    "DA": "110",
    "AMD": "111",
    "MDA": "111",
    "DAM": "111",
    "DMA": "111",
    "ADM": "111",
    "MAD": "111",
}

JUMP = {
    "": "000",
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

def fillzero(number,maxlenofnum):
    return str(number).rjust(maxlenofnum,"0")  #左边补0

def deleteNone(strcode):
    return str(strcode).replace("None","")

def writeintofile(filename,strlists):
    with open(filename,"w+") as wfile:
        for strlist in strlists:
            wfile.write(strlist + '\n')

def converttobin(number):
    return str(bin(number)).replace("0b","")
