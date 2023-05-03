'''
运算操作
'''
import sys
sys.path.append("../core")
import numpy as np
from Node import Node
class ADD(Node):
    # 矩阵加法
    def compute(self):
        self.value = np.zeros(self.parents[0].shape())
        for parent in self.parents:
            self.value += parent.value

class MatMul(Node):
    '''
    矩阵乘法
    '''
    def compute(self):
        assert len(self.parents == 2) and self.parents[0].shape()[
            1] == self.parents[1].shape()[0]
        self.value = self.parents[0].value * self.parents[1].value