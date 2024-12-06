import numpy as np

score = np.array([85, 90, 78, 92, 88], dtype=float)
a_score = score.copy()
a_score += 5

shape = score.shape
ndim = score.ndim
size = score.size
itemsize = score.itemsize
dtype = score.dtype
sorted_score = np.sort(score)

indices_80_plus = np.where(score > 80)[0]

min_val = score.min()
max_val = score.max()
std_dev = score.std()
variance = score.var()
total_sum = score.sum()
mean_val = score.mean()

print("score[::2]:", score[::2])
print("score[-3::-1]:", score[-3::-1])
print("score[1:4]:", score[1:4])

print("Original score:", score)
print("Modified a_score:", a_score)
print("Shape:", shape)
print("Number of dimensions:", ndim)
print("Size:", size)
print("Item size:", itemsize)
print("Data type:", dtype)
print("Sorted score:", sorted_score)
print("Indices with score > 80:", indices_80_plus)
print("Min:", min_val, "Max:", max_val)
print("Standard deviation:", std_dev)
print("Variance:", variance)
print("Sum:", total_sum)
print("Mean:", mean_val)
