import numpy as np

A = np.array([[1, 1, 1], [2, 3, 5], [4, 0, 5]])
B = np.array([6, -4, 27])

try:
    solution = np.linalg.solve(A, B)
except np.linalg.LinAlgError:
    solution = "Hệ phương trình không có nghiệm hoặc có vô số nghiệm"

print("Nghiệm của hệ phương trình:\n", solution)
