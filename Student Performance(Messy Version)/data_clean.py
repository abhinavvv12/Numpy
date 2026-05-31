import numpy as np

def clean_data(data):
    # Step-1
    # print(data)
    print("Nan count:", np.isnan(data).sum())
    print("Inf count:", np.isinf(data).sum())

    # Step-2
    # get indices of inf values
    row,col = np.where(np.isinf(data))
    # Replace each inf value with zero
    data[row , col] = 0

    # Step-3
    # Mean for every column
    col_mean = np.nanmean(data,axis = 0)

    # Step-4
    # get Indices of Nan values
    rows, cols = np.where(np.isnan(data))
    # Replace each Nan with its column mean
    data[rows , cols] = col_mean[cols]

    # step-5
    # Remove outliers
    mean = np.mean(data,axis = 0)
    std = np.std(data,axis = 0)

    # calculate z score for each column
    z_scores = (data-mean)/std #broadcasting takes care of it

    # print(z_scores)
    mask = np.all(np.abs(z_scores) < 3, axis = 1)
    cleaned_data = data[mask]
    return cleaned_data

data = np.genfromtxt("Student Performance(Messy Version)/students_messy.csv",delimiter=",",skip_header=1)

ans = clean_data(data)
print(ans)

print("Average per Subject: ", np.mean(ans,axis = 0))
totals = np.sum(ans,axis = 1)
top_index = np.argmax(totals)
print(top_index)
print("Top student: ", ans[top_index])
print("Removed students:", len(data)-len(ans))

totals = np.sum(ans,axis = 1)
rank_indices = np.argsort(-totals)
print("Ranking Students(Best to worst): ")
for rank,idx in enumerate(rank_indices, start =1):
    print(f"Rank {rank}: Student {idx} -> Total = {totals[idx]}")
def assign_grade(total):
    if total>=90:
        return "A"
    elif total>=75:
        return "B"
    elif total>=60:
        return "C"
    else:
        return "D"
for i,total in enumerate(totals):
    grade = assign_grade(total/3)
    print(f"Student {i}: Grade {grade}")







