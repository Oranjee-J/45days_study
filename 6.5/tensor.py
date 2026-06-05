import torch
tensor = torch.tensor([[1,2,3],[4,5,6]],dtype = torch.float32)

print('Tensor:\n', tensor)
print('Shape:\n',tensor.shape)
print('Size:',tensor.size())
print("Data Type:", tensor.dtype)
print("Device:", tensor.device)
print("Dimensions:", tensor.dim())
print("Total Elements:", tensor.numel())
print("Requires Grad:", tensor.requires_grad)
print("Is CUDA:", tensor.is_cuda)
print("Is Contiguous:", tensor.is_contiguous())

single_value = torch.tensor(42)
print("Single Element Value:", single_value.item())

tensor_T = tensor.T
print("Transposed Tensor:\n", tensor_T)