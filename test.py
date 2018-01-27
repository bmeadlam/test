class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if len(A) == 0:
            return
        c_z = {}
        r_z = {}
        for i, row in enumerate(A):
            for j, el in enumerate(row):
                if el == 0:
                    r_z[i] = True
                    c_z[j] = True
        for i in r_z.keys():
            for k in range(len(A[0])):
                A[i][k] = 0
        for j in c_z.keys():
            for k in range(len(A)):
                A[k][j] = 0
        return A
