from Node import *
import numpy as np
class Variable(Node):
    '''
    几点变量
    '''
    def __init__(self, dim, init = False, trainable = True, **kwargs):
        '''

        :param dim: 节点的维度，是一个二元的列表
        :param init:
        :param trainable:节点是否可以训练
        :param kwargs: others key = value
        '''
        Node.__init__(self,**kwargs)
        self.dim = dim
        if init:
            self.value = np.random.normal(0,0.001,self.dim)

        self.trainable = trainable

    def set_value(self,value):
        assert isinstance(value,np.ndarray) and value.shape == self.dim
        self.value = value #Todo