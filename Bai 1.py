import numpy as np

# Tạo hai ma trận ngẫu nhiên A và B kích thước 3x3
matrix_a = np.random.randint(0, 10, (3, 3))
matrix_b = np.random.randint(0, 10, (3, 3))

# Tính tổng, hiệu, tích và tích Hadamard của A và B
sum_matrix = np.add(matrix_a, matrix_b)
diff_matrix = np.subtract(matrix_a, matrix_b)
product_matrix = np.dot(matrix_a, matrix_b)
hadamard_product = np.multiply(matrix_a, matrix_b)

# Tính định thức của ma trận A
determinant_a = np.linalg.det(matrix_a)

# Tính ma trận nghịch đảo của A, nếu có
try:
    inverse_a = np.linalg.inv(matrix_a)
except np.linalg.LinAlgError:
    inverse_a = "Ma trận không có nghịch đảo"

# Tính ma trận chuyển vị của A
transpose_a = np.transpose(matrix_a)

# Tính giả nghịch đảo Moore-Penrose của ma trận A
moore_penrose_a = np.linalg.pinv(matrix_a)

# Tính chuẩn Frobenius của ma trận A
frobenius_norm_a = np.linalg.norm(matrix_a, 'fro')

# Tính norm L1 và L2 của mỗi hàng trong ma trận A
l1_norm = np.linalg.norm(matrix_a, 1, axis=1)
l2_norm = np.linalg.norm(matrix_a, 2, axis=1)

# Tìm ma trận con 2x2 nằm ở góc trên bên trái của ma trận A
submatrix_2x2 = matrix_a[:2, :2]

# Thực hiện phép nhân vô hướng của ma trận A với số vô hướng α = 2
scalar_multiplication = 2 * matrix_a

# Tính ma trận đối xứng A^T * A từ ma trận A
symmetric_matrix = np.dot(matrix_a.T, matrix_a)

# Tính tổng của các phần tử trên đường chéo chính của ma trận A (trace của ma trận)
trace_a = np.trace(matrix_a)

# Tìm các trị riêng và vector riêng của ma trận A
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)

# Kiểm tra xem ma trận A có khả năng chéo hóa không (nếu có đủ trị riêng phân biệt)
is_diagonalizable = len(np.unique(eigenvalues)) == matrix_a.shape[0]

# Tạo ma trận C có kích thước 3x3 với tất cả các phần tử bằng 1, sau đó cộng với A
matrix_c = np.ones((3, 3)) + matrix_a

# Tạo ma trận đường chéo từ các phần tử của một vector ngẫu nhiên có kích thước 3
random_vector = np.random.randint(0, 10, 3)
diagonal_matrix = np.diag(random_vector)

# Kiểm tra xem ma trận A có phải là ma trận trực giao không
is_orthogonal = np.allclose(np.dot(matrix_a, matrix_a.T), np.eye(matrix_a.shape[0]))

# Tạo ma trận vuông D kích thước 4x4 với các phần tử ngẫu nhiên
matrix_d = np.random.randint(0, 10, (4, 4))

# Tính ma trận D^(-1) (nếu có), và kiểm tra tính khả nghịch
try:
    inverse_d = np.linalg.inv(matrix_d)
    is_invertible_d = True
except np.linalg.LinAlgError:
    inverse_d = "Ma trận không có nghịch đảo"
    is_invertible_d = False

# Tính ma trận D nhân với chính nó và so sánh với ma trận vuông E nhân với E^(-1)
matrix_e = np.random.randint(0, 10, (4, 4))
product_dd = np.dot(matrix_d, matrix_d)
try:
    inverse_e = np.linalg.inv(matrix_e)
    product_ee_inv = np.dot(matrix_e, inverse_e)
except np.linalg.LinAlgError:
    product_ee_inv = "Không thể tính do ma trận E không khả nghịch"

# Tính ma trận D^T * B * A và tìm định thức của ma trận D
transpose_d = matrix_d.T
matrix_dba = np.dot(transpose_d, np.dot(matrix_b, matrix_a))
determinant_d = np.linalg.det(matrix_d)

# Tạo ma trận D nhân với ma trận đơn vị I_4 có cùng kích thước
identity_4 = np.eye(4)
product_d_identity = np.dot(matrix_d, identity_4)

# Tạo ma trận vuông F kích thước 3x3 với các phần tử trên đường chéo chính là các giá trị của một vector ngẫu nhiên
vector_random_f = np.random.randint(0, 10, 3)
matrix_f = np.diag(vector_random_f)

# Tính ma trận D^T * B * A và tìm định thức của ma trận D lần nữa
determinant_d_again = np.linalg.det(matrix_dba)

# Tính giả nghịch đảo Moore-Penrose của D
moore_penrose_d = np.linalg.pinv(matrix_d)

# Kiểm tra xem ma trận F có phải là ma trận trực giao không
is_f_orthogonal = np.allclose(np.dot(matrix_f, matrix_f.T), np.eye(matrix_f.shape[0]))

# Tính tích của F với ma trận đơn vị I_3 và kiểm tra xem kết quả có bằng chính ma trận F không
identity_3 = np.eye(3)
product_f_identity = np.dot(matrix_f, identity_3)
is_f_equal_to_itself = np.allclose(product_f_identity, matrix_f)

# Tính trace của ma trận F
trace_f = np.trace(matrix_f)

# In kết quả
print("Ma trận A:\n", matrix_a)
print("Ma trận B:\n", matrix_b)
print("Tổng của hai ma trận:\n", sum_matrix)
print("Hiệu của hai ma trận:\n", diff_matrix)
print("Tích của hai ma trận:\n", product_matrix)
print("Tích Hadamard của hai ma trận:\n", hadamard_product)
print("Định thức của ma trận A:\n", determinant_a)
print("Ma trận nghịch đảo của A:\n", inverse_a)
print("Ma trận chuyển vị của A:\n", transpose_a)
print("Giả nghịch đảo Moore-Penrose của ma trận A:\n", moore_penrose_a)
print("Chuẩn Frobenius của ma trận A:\n", frobenius_norm_a)
print("Norm L1 của mỗi hàng trong ma trận A:\n", l1_norm)
print("Norm L2 của mỗi hàng trong ma trận A:\n", l2_norm)
print("Ma trận con 2x2 của ma trận A:\n", submatrix_2x2)
print("Phép nhân vô hướng của ma trận A với α = 2:\n", scalar_multiplication)
print("Ma trận đối xứng A^T * A:\n", symmetric_matrix)
print("Tổng của các phần tử trên đường chéo chính của ma trận A (trace):\n", trace_a)
print("Trị riêng của ma trận A:\n", eigenvalues)
print("Vector riêng của ma trận A:\n", eigenvectors)
print("Ma trận A có khả năng chéo hóa không:", is_diagonalizable)
print("Ma trận C (3x3 với tất cả phần tử bằng 1, cộng với A):\n", matrix_c)
print("Ma trận đường chéo từ vector ngẫu nhiên:\n", diagonal_matrix)
print("Ma trận A có phải là ma trận trực giao không:", is_orthogonal)
print("Ma trận D:\n", matrix_d)
print("Ma trận nghịch đảo của D (nếu có):\n", inverse_d)
print("Ma trận D nhân với chính nó:\n", product_dd)
print("Ma trận E nhân với E^(-1):\n", product_ee_inv)
print("Ma trận D^T * B * A:\n", matrix_dba)
print("Định thức của ma trận D:\n", determinant_d)
print("Ma trận D nhân với ma trận đơn vị I_4:\n", product_d_identity)
print("Ma trận F (đường chéo chính từ vector ngẫu nhiên):\n", matrix_f)
print("Định thức của ma trận D^T * B * A:\n", determinant_d_again)
print("Giả nghịch đảo Moore-Penrose của D:\n", moore_penrose_d)
print("Ma trận F có phải trực giao không:", is_f_orthogonal)
print("Tích của F với ma trận đơn vị I_3:\n", product_f_identity)
print("Kết quả có bằng chính ma trận F không:", is_f_equal_to_itself)
print("Trace của ma trận F:\n", trace_f)