def pal(A):
    if len(A) == 1:
        return [[A]]
    # print(A[-1])
    # print(A[:-1])
    return merge(A[-1], pal(A[:-1]))


def merge(ch, s):
    out = []
    for pal_list in s:
        for i in range(len(pal_list)):
            if is_pal(sum_list(pal_list[-i:]) + ch):
                out.append(pal_list[:-i] + [sum_list(pal_list[-i:]) + ch])
        out.append(pal_list + [ch])
    return out


def is_pal(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            return False
    return True


def sum_list(l):
    out = ''
    for x in l:
        out = out + x
    return out


# print(pal('efe'))
print(pal('efe'))
