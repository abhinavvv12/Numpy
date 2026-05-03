import numpy as np

def clean_data(arr):
    print("Number of Nan Values:", np.isnan(arr).sum())
    print("Number of Inf values:", np.isinf(arr).sum())

    arr[np.isinf(arr)] = 0

    mean = np.nanmean(arr)

    arr[np.isnan(arr)] = mean

    mean = np.mean(arr)
    std = np.std(arr)
    z = (arr-mean)/std

    cleaned_arr = arr[np.abs(z)<3]
    return cleaned_arr


arr = np.array([10,20,30,np.nan, np.nan, 60,70, np.inf, -np.inf, 90, 100])
final_arr = clean_data(arr)
print("final cleaned data:", final_arr)








