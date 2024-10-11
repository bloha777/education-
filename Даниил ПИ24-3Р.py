import numpy as np


A = np.array([[6, 3, -2], [5, -8, 4], [1, -6, 0]])
B = np.array([[-3, 1, 2]])
C = np.array([[8, 2], [3, 0], [4, -2]])
D = np.array([[0, 1], [2, 4], [7, -1]])

result_a_1 = 2 * C + 5 * D
result_a_2 = C - 3 * D

try:
    B_inv_3 = np.linalg.inv(B)
except np.linalg.LinAlgError:
    B_inv_3 = "B3 не обратимая матрица"

result_c_AB_3 = np.dot(A, B.T)
result_c_BC_3 = np.dot(B, C)

try:
    A_inv_3 = np.linalg.inv(A)
except np.linalg.LinAlgError:
    A_inv_3 = "A3 не обратимая матрица"

print("a) 2C + 5D:", result_a_1)
print("a) C - 3D:", result_a_2)

print("\nИнверсия матрицы B:", B_inv_3)

print("\nAB (умножение A и B):", result_c_AB_3)
print("BC (умножение B и C):", result_c_BC_3)

print("\nОбратная матрица для A:", A_inv_3)