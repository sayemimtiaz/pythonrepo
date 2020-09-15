import torch.nn as nn

class CustomModule(nn.Module):
  def __init__(self):
      self.conv1 = nn.Conv2d(1, 20, 5)     # Add key conv1 to self._modules
      self.conv2 = nn.Conv2d(20, 20, 5)  
