
import torch
'''

a way to show the data in a better format

'''

def loggerTensor(data:torch.Tensor,name:str = ""):
    print("==========={str}==============".format(str = name))
    print("size:{size}".format(size = str(data.shape)) + "\t type:{type}".format(type = str(data.dtype)) + "\t device:{device}".format(device = str(data.device)))
    print(data)
    print("==========={str}==============".format(str = name))