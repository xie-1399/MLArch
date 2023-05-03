#demo of adline
import numpy as np
from core import Variable
from ops import ops

Variable = Variable.Variable
male_heights = np.random.normal(176,6,500)
male_weights = np.random.normal(70,10,500)

female_heights = np.random.normal(168,5,500)
female_weights = np.random.normal(50,6,500)

#Label
male_labels = [1] * 500
female_labels = [-1] * 500

train_set = np.array([np.concatenate((male_heights,female_heights)),
                      np.concatenate((male_weights,female_weights)),np.concatenate((male_labels,female_labels))])
np.random.shuffle(train_set) #shuffle

x = Variable(dim=(2, 1), init=True, trainable=False)
w = Variable(dim=(1, 2), init=True, trainable=True)
b = Variable(dim=(1, 1), init=True, trainable=True)

#重写抽象方法（进行计算）
output = ops.ADD(ops.MatMul(w, x), b)
print(output)