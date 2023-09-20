
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor,Lambda,Compose


'''

this file contains how to use torch to create the whole model step by step(quick start)
the material is from pytorch manual in getting start
so the whole step likely: process data -> create Model -> define the loss function and optimizer -> then train and test it -> save model
in fact from this see the network process is the similar way

'''

# show about the available gpu
def UsingDevice():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using {} device".format(device))
    return device

# gen the process dataset and split them
def GenData(download,batchSize = 16,raw = False,witnshape = True):
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=download,
        transform=ToTensor()
    )

    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=download,
        transform=ToTensor()
    )
    train_dataloader = DataLoader(training_data,batch_size = batchSize)
    test_dataloader = DataLoader(test_data,batch_size = batchSize)
    if witnshape:
        for x,y in test_dataloader:
            print("Shape of X [N, C, H, W]: ", x.shape)
            print("Shape of y: ", y.shape, y.dtype)
            break
    if raw:
        return training_data, test_data
    else:
        return train_dataloader, test_dataloader

def logger(infor):
    print(infor)

# this show about how to create model using the nn layer
class NeuralNetwork(nn.Module):

    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        # this is the simple way to define a linear network
        self.linear = nn.Sequential(
            nn.Linear(28 * 28,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,10)
        )

    def forward(self,x):
        x = self.flatten(x)
        logic = self.linear(x)
        return logic

def lossAndOptimal(model:nn.Module):
    loss_fn = nn.CrossEntropyLoss()
    oprimizer = torch.optim.SGD(model.parameters(),lr=1e-3)
    return loss_fn,oprimizer

# training the data looks like simple way
def train(trainloader,testloader,model,loss_fn,optimizer,epochs,saveModel = True):
    for epoch in range(epochs):
        size = len(trainloader.dataset)
        model.train() # show the train function

        for batch,(x,y) in enumerate(trainloader):
            x,y = x.to(device),y.to(device)

            #calculate the loss
            pred = model(x)
            loss = loss_fn(pred,y)

            #back propagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 100 == 0:
                loss, current = loss.item(), batch * len(x)
                print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")

        # each epoch test about it
        size = len(testloader.dataset)
        num_batches = len(testloader)
        model.eval()
        test_loss,correct = 0,0
        with torch.no_grad():
            for x,y in testloader:
                x, y = x.to(device), y.to(device)
                pred = model(x)
                test_loss += loss_fn(pred,y).item()
                correct += (pred.argmax(1) == y).type(torch.float).sum().item()
        test_loss /= num_batches
        correct /= size
        print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    if(saveModel):
        torch.save(model.state_dict(),"./model.pth")
        print("================== save the pytorch model! ====================")

def inference(model,file,data,label):
    model.load_state_dict(torch.load(file))
    classes = [ "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal",
                "Shirt", "Sneaker", "Bag", "Ankle boot"]
    model.eval()
    with torch.no_grad():
        pred = model(data)
        predicted,actual = classes[pred[0].argmax(0)], classes[label]
        print(f'Predicted: "{predicted}", Actual: "{actual}"')


if __name__ == '__main__':
    train_dataloader,test_dataloader = GenData(download=False,batchSize=64)
    train_data,test_data = GenData(download=False,batchSize=64,raw=True)

    device = UsingDevice()
    model = NeuralNetwork().to(device)  # the model show lots of information about the network
    loss_fn, oprimizer = lossAndOptimal(model)
    # train(train_dataloader,test_dataloader,model,loss_fn,optimizer,epochs=5)

    inference(model,"./model.pth",torch.as_tensor(test_data[0][0]).to(device),torch.as_tensor(test_data[0][1]).to(device))
