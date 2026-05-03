"""
reshape(rows,colums) specify new shape
if dimensions match
"""

import numpy as np
arr = np.array([1,2,3,4,5,6])

reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

# reshaping does not create copy
# it is a view
# if changes are made in arr, it affects reshaped_arr