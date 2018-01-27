

def rot_cyc(mat, i, j, n):
    dum = mat[i][j]
    for _ in range(3):
        mat[i][j] = mat[n-1-j][i]
        i, j = n-1-j, i
    mat[i][j] = dum
    return mat


def rot_mat(mat):
    n = len(mat)
    for i in range(int(n/2)):
        for j in range(i, n-i-1):
            mat = rot_cyc(mat, i, j, n)
    return mat


def print_mat(mat):
    for row in mat:
        print(row)
    print('\n')


mat = []
for i in range(10):
    mat.append([1 + j + 10*i for j in range(10)])
print_mat(mat)
print_mat(rot_mat(mat))
