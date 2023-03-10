#test torch 1.12.1 + cu113
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)

#Torch计算图
leaf1 = torch.tensor([1.],requires_grad=True)
leaf2 = torch.tensor([2.],requires_grad=True)
#求导机制,只保存叶子节点的梯度，非叶子节点会被释放
node1 = torch.add(leaf2,leaf1)
node2 = torch.sub(leaf2,1)
root = torch.matmul(node1,node2)
root.backward()
print("leaf1 grad:",leaf1.grad)
print("leaf2 grad:",leaf2.grad)

