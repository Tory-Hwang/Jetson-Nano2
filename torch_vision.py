import torch
import torchvision

print( "torch ver:", torch.__version__ )
print( "torchvision ver:",torchvision.__version__)

print("CUDA Used:", torch.cuda.is_available())

