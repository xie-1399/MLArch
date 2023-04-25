'''
进行正向微分：这里使用了运算符号的重载，就是每正向传播一次就需要进行微分值的计算
'''
import numpy as np
class ADTangent:
    def __init__(self,x,dx):
        self.x = x
        self.dx = dx
    def __str__(self):
        context = 'value:{value},grad:{grad}'.format(value = self.x , grad = self.dx )
        return context

    #重载+符号
    def __add__(self, other):
        if isinstance(other,ADTangent):
            x = self.x + other.x
            dx = self.dx + other.dx
        elif isinstance(other,float):
            x = self.x + other
            dx = self.dx
        else:
            raise NotImplementedError("__add__ not implement")
        return ADTangent(x,dx)

    def __sub__(self, other):
        if isinstance(other,ADTangent):
            x = self.x - other.x
            dx = self.dx - other.dx
        elif isinstance(other,float):
            x = self.x - other
            dx = self.dx
        else:
            raise NotImplementedError("__sub__ not implement")
        return ADTangent(x,dx)

    def __mul__(self, other):
        if isinstance(other,ADTangent):
            x = self.x * other.x
            dx = self.dx * other.x + other.dx * self.x
        elif isinstance(other,float):
            x = self.x * other
            dx = self.dx * other
        else:
            raise NotImplementedError("__mul__ not implement")
        return ADTangent(x,dx)

    #Just agent can compute like this
    def log(self):
        x = np.log(self.x)
        dx = (1 / self.x) * self.dx
        return ADTangent(x, dx)
    def sin(self):
        x = np.sin(self.x)
        dx = np.cos(self.x) * self.dx
        return ADTangent(x, dx)

if __name__ == '__main__':
    temp1 = ADTangent(2.0,1)
    temp2 = ADTangent(5.0,0)
    #func = ADTangent.log(temp1) + temp1 * temp2 - ADTangent.sin(temp2)
    func = temp1.log() + temp1 * temp2 - temp2.sin()
    print(func)