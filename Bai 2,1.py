import numpy as np

coeff_matrix = np.array([[2, 3, 1], [4, 1, 5], [3, 2, 4]])
const_matrix = np.array([1, 2, 3])

try:
    inverse_coeff = np.linalg.inv(coeff_matrix)
    solution = np.dot(inverse_coeff, const_matrix)
except np.linalg.LinAlgError:
    solution = "Hệ phương trình không có nghiệm do ma trận không khả nghịch"

print("Nghiệm của hệ phương trình:\n", solution)