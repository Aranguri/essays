import numpy as np
A = np.array([[1, 2], [2, 4]])
I = np.eye(2)

for a in np.logspace(0, -8, 10):
    inner = A.T.dot(A) + a * I
    inner = np.linalg.inv(inner).dot(A.T)
    print(inner)
