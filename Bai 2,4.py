import numpy as np

A = np.array([[2, -3, 1], [4, -6, 2], [-1, 3, -1]])
B = np.array([5, 10, -3])

rank_A = np.linalg.matrix_rank(A)
augmented_matrix = np.hstack((A, B.reshape(-1, 1)))
rank_augmented = np.linalg.matrix_rank(augmented_matrix)

if rank_A == rank_augmented:
    if rank_A == A.shape[1]:
        solution = np.linalg.solve(A, B)
        print("Hệ phương trình có nghiệm duy nhất:\n", solution)
    else:
        print("Hệ phương trình có vô số nghiệm.")
else:
    print("Hệ phương trình vô nghiệm.")
