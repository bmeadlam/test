

def uni_char_q(s):
    char_hash = {}

    for c in s:
        try:
            char_hash[c]
            return True
        except:
            char_hash[c] = 1

    return False


print(uni_char_q(''))
print(uni_char_q('abc'))
print(uni_char_q('abcdefga'))
