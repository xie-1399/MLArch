'''
自动微分：如何反向进行
'''
from typing import NamedTuple, List, Callable
import numpy as np

_name = 1
def fresh_name():
    global _name
    name = str(_name)
    _name += 1
    return name

class Variable_(object):
    def __init__(self,value,name = None): # Name?
        self.value = value
        self.name = name or fresh_name() #节点名字

    def __str__(self):
        return "value : {value}".format(name = self.name , value = self.value)

    def __mul__(self, other):
        return ops_mul(self,other)

    def __add__(self, other):
        return ops_add(self, other)

    def __sub__(self, other):
        return ops_sub(self, other)

    def sin(self):
        return ops_sin(self)

    def log(self):
        return ops_log(self)

    @staticmethod
    def constant(value,name = None):
        return Variable_(value,name)
#表示函数与变量之间的关系的一种数据结构
class Tape(NamedTuple):
    input:List[str]
    output:List[str]
    #chain rule
    propagate:Callable

class Tape_New(object):
    def __init__(self, input, output, propagate):
        self.input = input
        self.output = output
        self.propagate = propagate

gradient_tape : List[Tape] = []
def reset_tape():
    global _name
    _name = 1
    gradient_tape.clear()


#乘法的反向自动微分
def ops_mul(self,other):
    #foreward
    result = Variable_(self.value * other.value)
    #add to the Tape
    def propagate(dl_doutputs):
        dl_dx, = dl_doutputs
        dx_dself = other  # partial derivate of r = self*other
        dx_dother = self  # partial derivate of r = self*other
        dl_dself = dl_dx * dx_dself
        dl_dother = dl_dx * dx_dother
        dl_dinputs = [dl_dself, dl_dother]
        return dl_dinputs

    tape = Tape(input=[self.name,other.name],output=[result.name],propagate = propagate)
    gradient_tape.append(tape)
    return result


def ops_add(self, other):
    # foreward
    result = Variable_(self.value + other.value)
    # add to the Tape
    def propagate(dl_doutputs):
        dl_dx, = dl_doutputs
        dx_dself = Variable_(1.0)
        dx_dother = Variable_(1.0)
        dl_dself = dl_dx * dx_dself
        dl_dother = dl_dx * dx_dother
        dl_dinputs = [dl_dself, dl_dother]
        return dl_dinputs

    tape = Tape(input=[self.name,other.name],output=[result.name],propagate = propagate)
    gradient_tape.append(tape)
    return result


def ops_sub(self, other):
    # foreward
    result = Variable_(self.value - other.value)
    # add to the Tape
    def propagate(dl_doutputs):
        dl_dx, = dl_doutputs
        dx_dself = Variable_(1.0)
        dx_dother = Variable_(-1.0)
        dl_dself = dl_dx * dx_dself
        dl_dother = dl_dx * dx_dother
        dl_dinputs = [dl_dself, dl_dother]
        return dl_dinputs

    tape = Tape(input=[self.name,other.name],output=[result.name],propagate = propagate)
    gradient_tape.append(tape)
    return result


def ops_sin(self):
    # foreward
    result = Variable_(np.sin(self.value))
    # add to the Tape
    def propagate(dl_doutputs):
        dl_dx, = dl_doutputs
        dl_dself = dl_dx * Variable_(np.cos(self.value))
        dl_dinputs = [dl_dself]
        return dl_dinputs

    tape = Tape(input=[self.name],output=[result.name],propagate = propagate)
    gradient_tape.append(tape)
    return result

def ops_log(self):
    # foreward
    result = Variable_(np.log(self.value))

    # add to the Tape
    def propagate(dl_doutputs):
        dl_dx, = dl_doutputs
        dl_dself = dl_dx * Variable_(1 / self.value)
        dl_dinputs = [dl_dself]
        return dl_dinputs

    tape = Tape(input=[self.name],output=[result.name],propagate = propagate)
    gradient_tape.append(tape)
    return result

#根据Tape计算梯度,Need to understand
def grad(l,results,showall=False):
    dl_d = {}  # map dL/dX for all values X
    dl_d[l.name] = Variable_(1.)

    def gather_grad(entries):
        return [dl_d[entry] if entry in dl_d else None for entry in entries]

    for entry in reversed(gradient_tape):
        if(showall):
            print(entry)
        dl_doutputs = gather_grad(entry.output)
        dl_dinputs = entry.propagate(dl_doutputs)

        for input, dl_dinput in zip(entry.input, dl_dinputs): #返回元组列表
            if input not in dl_d:
                dl_d[input] = dl_dinput
            else:
                dl_d[input] += dl_dinput

    return gather_grad(result.name for result in results)

if __name__ == '__main__':
    #Forward
    reset_tape()
    x = Variable_.constant(2., name='v-1')
    y = Variable_.constant(5., name='v0')
    f = Variable_.log(x) + x * y - Variable_.sin(y)
    print(f)
    #Backward
    dx, dy = grad(f, [x, y])
    print("dx", dx)
    print("dy", dy)