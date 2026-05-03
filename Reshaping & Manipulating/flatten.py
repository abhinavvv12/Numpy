"""
.ravel() ->view
.flatten() ->copy
"""
import numpy as np

arr_2d = np.array([[2,3],[5,6]])
print(arr_2d.flatten())
print(arr_2d.ravel())
print(arr_2d)