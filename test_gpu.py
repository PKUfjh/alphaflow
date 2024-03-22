import torch
print(torch.cuda.is_available())

ckpt = torch.load('./weights/alphaflow_pdb_base_202402.pt', map_location='cpu')
print(ckpt.keys())
