#计算图节点基类
import abc


class Node(object):
    '''
    节点基类
    '''
    def __init__(self,*parents,**kwargs):  #tuple/键值对

        self.value = None
        self.parents = list(parents)  #父节点
        self.children = []

        #本节点需要当作父节点的子节点
        for parent in self.parents:
            parent.children.append(self)

    def __str__(self):
        return  "Value : " + str(self.value)

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


    def dimension(self):
        #Return dimension
        return self.value.shape[0] * self.value.shape[1]

    def shape(self):
        return self.value.shape

    def reset_value(self, recursive = True):
        # Reset the value
        self.value = None
        if(recursive):
            for child in self.children:
                child.reset_value()
    @abc.abstractmethod
    def compute(self):
        pass
