import numpy as np

A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
B = np.array([1, 0, 1])

try:
    solution = np.linalg.solve(A, B)
    print("Nghiệm của hệ phương trình:\n", solution)
except np.linalg.LinAlgError:
    print("Hệ phương trình không có nghiệm duy nhất hoặc có vô số nghiệm.")
