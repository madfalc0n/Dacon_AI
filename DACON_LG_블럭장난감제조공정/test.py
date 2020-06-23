import numpy as np

def relu(z):
    return z * (z > 0)

print(relu(5))