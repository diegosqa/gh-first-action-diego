import numpy as np

print("Startin traininig simulation...")
data= np.random.rand(100)
print("Mean: ", data.mean())

raise RuntimeError("Simulated training failure")
