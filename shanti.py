import numpy as np

data=[
    [23,45,67,89,98],
    [22,33,43,25,66],
    [56,98,67,43,90],
    [24,88,57,94,88]
    ]
result=np.array(data)
"""print(result.shape)
print(result.size)
print(result.ndim)
print(result.dtype)
print(type(result)) """

average=np.mean(result,axis=0)
total=np.sum(result,axis=1)
overall=np.mean(result)
highest=np.max(result)
lowest=np.min(result)

print(average)
print(total)
print(overall)
print(highest)
print(lowest)