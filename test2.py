

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, S, L):
        # check that S and L are not empty
        if len(S) == 0 or len(L) == 0:
            return None

        word_len = len(L[0])

        out_inds = []
        for start in range(word_len):
            # split string
            arr_S = split_S(S, start, word_len)

            # build hash table for L
            H = {}
            for s in L:
                try:
                    H[s] += 1
                except:
                    H[s] = 1

            # initialize start of search
            s = 0
            while s < len(arr_S):
                if hash_Q(H, arr_S[s]):
                    if H[arr_S[s]] > 1:
                        H[arr_S[s]] -= 1
                    else:
                        del H[arr_S[s]]
                    if len(H.keys()) == 0:
                        out_inds.append(start + s * word_len)
                    break
                else:
                    s += 1
            e = s+1

            # search
            while s < len(arr_S) and e < len(arr_S):
                if s > e:
                    e += 1
                elif hash_Q(H, arr_S[e]):
                    if H[arr_S[e]] > 1:
                        H[arr_S[e]] -= 1
                    else:
                        del H[arr_S[e]]
                    e += 1
                else:
                    if s < e:
                        try:
                            H[arr_S[s]] += 1
                        except:
                            H[arr_S[s]] = 1
                    s += 1
                if len(H.keys()) == 0:
                    out_inds.append(start + s * word_len)
        return out_inds


def hash_Q(H, key):
    try:
        H[key]
        return True
    except:
        return False


def split_S(S, start, word_len):
    out = []
    for i in range(start, len(S) + 1 - word_len, word_len):
        out.append(S[i: i + word_len])
    return out


sol = Solution()
print(sol.findSubstring('aaaaa', ['a', 'a']))
