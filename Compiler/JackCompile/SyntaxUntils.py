#词法分析的一些工具类
import re

keyWords = [
    "CLASS",
    "DO",
    "IF",
    "ELSE",
    "WHILE",
    "RETURN",
    "FUNCTION",
    "CONSTRUCTOR",
    "INT",
    "BOOLEAN",
    "CHAR",
    "METHOD",
    "VOID",
    "VAR",
    "STATIC",
    "FIELD",
    "LET",
    "TRUE",
    "FALSE",
    "NULL",
    "THIS"
]

Identifier = re.compile("^\s*([a-zA-Z_][a-zA-Z_1-9]*)\s*")  #注意/s会匹配对应的空白

Signal = []
