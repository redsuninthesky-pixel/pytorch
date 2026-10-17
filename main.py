#day 1
import torch
import numpy as np
data =[[1,2],[3,4]]
x_data = torch.tensor(data)
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
x_ones = torch.ones_like(x_data)
#print(f"Tensor \n {x_ones} \n")
x_rand = torch.rand_like(x_data,dtype=torch.float)
#print(x_rand)

shape = (2,3)
forced_dimension = torch.rand(shape)
#print(forced_dimension)

print(forced_dimension.shape)
print(forced_dimension.dtype)
print(forced_dimension.device)
