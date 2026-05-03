"""
slicing - (start,stop,step) 
stop is excluded
default step values is 1

arr[start:end], start to end -1
"""
import numpy as np

arr = np.array([10,20,30,40,50])
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 4
print(arr[::2]) #start to end, with step size 
print(arr[::-1])#reverse array

