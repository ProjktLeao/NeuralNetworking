import MainFrameWork as Framework

X = [2,3,4,5]

Layer1 = Framework.Network.layer(3,4)

Layer1.Forward(X, "ReLU")
print (Layer1.Output)