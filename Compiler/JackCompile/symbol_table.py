from Compiler.JackCompile import consts


class Content(object):
    '''
    符号表字段
    '''
    def __init__(self, type: str, kind: str , num: int):
        self.type = type
        self.kind = kind
        self.num = num

    def __str__(self):
        if self.type and self.num:
            return self.type + "--" + self.kind + "--" + str(self.num) + "--"
        else:
            return ""

class Table(object):
    def __init__(self) -> None:
        self.data: dict[str, Content] = {}
        self.counters = {
            "STATIC": 0,
            "FIELD": 0,
            "ARG": 0,
            "VAR": 0
        }
    def add(self, name: str, type: str, kind: str) -> None:
        self.data[name] = Content(type, kind, self.counters[kind])
        self.counters[kind] += 1

    def __str__(self):
        #show the symbolTable
        try:
            return self.data.keys()
        except Exception:
            return "Table Error!"

class SymbolTable(object):

    '''
    :符号表，用于处理对象、数组和变量，或者直接理解为是进行数据翻译
    :但是需要对不同的类或者子方法中的table进行重新构建
    '''
    def __init__(self):
        """Creates a new empty symbol table."""
        self.curr_class = ""
        self.curr_subrn = ""
        self.class_t =  Table()
        self.subr_t = Table()
    def start_subroutine(self,is_method: bool):
        '''
        : 每次调用一个方法都需要将对应的类加入到符号表中去
        :param is_method:
        :return:
        '''
        self.subr_t = Table()
        if is_method:
            self.subr_t.add("this", self.curr_class, "ARG")

    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns
        it a running index. "STATIC" and "FIELD" identifiers have a class scope,
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        # Your code goes here!
        if kind in ["STATIC", "FIELD"]:
            self.class_t.add(name, type, kind)
        elif kind in ["ARG", "VAR"]:
            self.subr_t.add(name, type, kind)

    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in
            the current scope.
        """
        # Your code goes here!
        return self.subr_t.counters[kind] + self.class_t.counters[kind]

    def _record_of(self, name: str):
        try:
            return self.subr_t.data[name]
        except KeyError:
            try:
                return self.class_t.data[name]
            except KeyError:
                # if the code is error free:
                # means that we encountered a subroutine name or a class name
                return None

    def kind_of(self, name: str) -> str:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        # Your code goes here!
        record = self._record_of(name)
        if record:
            return self._record_of(name).kind

    def segment_of(self, name: str) -> str:
        record = self._record_of(name)
        if record:
            return consts.KIND_TO_SEGMENT[
                self._record_of(name).kind
            ]

    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        # Your code goes here!
        record = self._record_of(name)
        if record:
            return self._record_of(name).type

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        # Your code goes here!
        record = self._record_of(name)
        if record:
            return self._record_of(name).num
