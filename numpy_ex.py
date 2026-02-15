import numpy as np

a = np.array([10,20,30,40])
print(a)
print("Hello World")
print(type(a))

mark_arr = np.array([72,85,90,66,88,95])
print(mark_arr.shape)
print(np.mean(mark_arr))
print(f"Max is: {np.max(mark_arr)} , Min is {np.min(mark_arr)}")

for mark in mark_arr:
    mark+=5

for mark in mark_arr:
    if mark>=85:
        print(mark)


arr = np.arange(1, 7)
print(arr)
new_arr = arr.reshape(2,3)
print(new_arr)

arr = np.array([[1,2],[3,4]])
flat = arr.flatten()
print(flat)

