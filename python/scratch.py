import numpy as np
rng=np.random.default_rng()

def count_new_infections(x):
    _, num_patches = x.shape
    total_cases = np.zeros(num_patches)

    for j in range(0,num_patches):
        daily_cases = x[:,j]
        total_cases[j] = daily_cases[0] + np.cumsum(np.maximum(np.diff(daily_cases),0))[-1]

    return total_cases

x = np.array([[1,2],[2,1],[3,5],[2,4]])
print(x)
print(count_new_infections(x))