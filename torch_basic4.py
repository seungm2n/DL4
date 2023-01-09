'''
    * 텐서(tensor)
        - 배열(array)이나 행렬(matrix)과 매우 유사한 특수한 자료구조
'''
# list로부터 tensor 생성하기   --- copy 본 생성
import torch
import numpy as np

data = [[1,2],[3,4]]
x_data = torch.tensor(data)
print(x_data)

# numpy array로부터 tensor 생성하기
np_array = np.array(data)
x_np_1 = torch.tensor(np_array)
print(x_np_1)

x_np_2 = torch.as_tensor(np_array)      # view를 만듦
print(x_np_2)

x_np_3 = torch.as_tensor(np_array)      # view를 만듦
print(x_np_3)

x_np_1[0, 0] = 5
print(x_np_1)
print(np_array)
print(x_np_2)
print(x_np_3)
