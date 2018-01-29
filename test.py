class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        walker = 0
        out = [walker]
        for delta in range(1, 2**A):
            walker = walker ^ (delta % 2**func(delta))
            walker = walker % 2**A
            out.append(walker)
        return out


def func(delta):
    cnt = 0
    for bit in reversed(bin(delta)):
        if bit == '0':
            cnt += 1
        else:
            return cnt + 1


sol = Solution()
print(sol.grayCode(10))
