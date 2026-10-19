import numpy as np
import matplotlib.pyplot as plt
#Ex 3
N_2_start = 3
N_2_end = 14
domain_size = 2 #number of grid points
N_ = np.array([2**i for i in range(N_2_start, N_2_end)])
print(f"resolutions: {N_}")
h = domain_size/N_
print(f"cell sizes: {h}")

diff_order=2
stencil_weights=np.array([[1/(2*h),0,-1/(2*h)],[1/(2*h),0,-1/(2*h)],[1/(h**2),-2*(h**2),1/(h**2)]])
