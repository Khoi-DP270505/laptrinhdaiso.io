import numpy as np

coeff_matrix = np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]], dtype=float)
const_matrix = np.array([7, 4, 5], dtype=float)

n = len(const_matrix)

# Phương pháp khử Gauss
for i in range(n):
    max_row = i + np.argmax(np.abs(coeff_matrix[i:, i]))
    coeff_matrix[[i, max_row]] = coeff_matrix[[max_row, i]]
    const_matrix[[i, max_row]] = const_matrix[[max_row, i]]

    for j in range(i + 1, n):
        factor = coeff_matrix[j, i] / coeff_matrix[i, i]
        coeff_matrix[j, i:] -= factor * coeff_matrix[i, i:]
        const_matrix[j] -= factor * const_matrix[i]

solution = np.zeros(n)
for i in range(n - 1, -1, -1):
    solution[i] = (const_matrix[i] - np.dot(coeff_matrix[i, i + 1:], solution[i + 1:])) / coeff_matrix[i, i]

print("Nghiệm của hệ phương trình:\n", solution)