
import torch
import numpy as np

from Network.Utils.logger import loggerTensor

'''

let's start from the tensor, this is the neural in the network
tensor defines the way of how to compute in the network
all input data / output data and parameters in the network should be tensor format
more tensor operation should look at the pytorch manual


'''

def tensorOperation():
    data =[[1,2],[3,4]]
    tensor_data = torch.tensor(data)
    loggerTensor(tensor_data)

    # also you can define it from the numpy
    np_array = np.array(data)
    nptotensor = torch.from_numpy(np_array)

    #or define from other tensors
    x_ones = torch.ones_like(tensor_data)
    loggerTensor(x_ones)
    x_rand = torch.rand_like(tensor_data,dtype=torch.float) # torch.dtype
    loggerTensor(x_rand)

    #index and indice
    tensor = torch.ones(4, 4)
    print('第一行: ', tensor[0])
    print('第一列：', tensor[:, 0])
    print('最后一列：', tensor[..., -1])
    tensor[:, 1] = 0
    print(tensor)

    #cat in the each dim
    t1 = torch.cat([tensor,tensor,tensor],dim = 0)
    t2 = torch.cat([tensor,tensor,tensor],dim = 1)
    loggerTensor(t1)
    loggerTensor(t2)

    #some common arith calculate way
    y1 = tensor @ tensor.T  #matrix mul
    y2 = tensor.matmul(tensor.T)
    y3 = torch.matmul(tensor,tensor.T)
    loggerTensor(y1)
    loggerTensor(y2)
    loggerTensor(y3)

    #dot point mul
    z1 = tensor * tensor
    z2 = tensor.mul(tensor)
    z3 = torch.mul(tensor,tensor)
    loggerTensor(z3, name = "z3")

    #change to common if tensor one dim
    agg = tensor.sum().item() #sum will sum all values -> one value
    print(agg)

    # operate one the variable
    tensor.add_(5)
    loggerTensor(tensor,name="tensor")


def convertNumpy():
    # tensor -> numpy,and the tensor change will change the numpy too
    tensor = torch.ones([2,3,4])
    n = tensor.numpy()

    #numpy -> tensor
    num = np.ones(5)
    tensor = torch.from_numpy(num)


if __name__ == '__main__':
    tensorOperation()