#计算图节点基类
import abc


class Node(object):
    def __init__(self,*parents,**kwargs):

        self.value = None
        self.parents = list(parents)  #父节点
        self.children = []

        #本节点需要当作父节点的子节点
        for parent in self.parents:
            parent.children.append(self)

    def get_parents(self):
        return self.parents

    def get_children(self):
        return self.children

    def forward(self):
        for node in self.parents:
            if(node.value != None):
                self.forward()

        self.compute()

    def backward(self):
        pass


    @abc.abstractmethod
    def compute(self):
        pass
class Variable(Node):
    pass