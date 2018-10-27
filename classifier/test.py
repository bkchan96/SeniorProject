import torch
from torch.autograd import Variable

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = Variable(torch.Tensor([1.0]), requires_grad=True) #sets w, a variable to a tensor containing 1.0


def forward(x):
    return x * w


def loss(x, y):
    y_pred = forward(x)
    return (y_pred-y)*(y_pred-y)


def gradient(x, y):
    return 2*x*(x*w-y)


print("predict (before training)", 4, forward(4))

for epoch in range(100):
    for x_val, y_val in zip(x_data, y_data):
        l = loss(x_val, y_val)
        l.backward() #Calculates computation of every value from loss going backwards to w
        print("\tgrad: ", x_val, y_val, w.grad.data[0]) #calculating the
        grad = gradient(x_val, y_val)
        w.data = w.data - 0.01 * w.grad.data

        w.grad.data.zero_()

        print("progress:", epoch, l.data[0])

print("predict(after training)", "4 hours", forward(4).data[0])
