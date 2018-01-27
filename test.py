

def uni_char_q(s):
    char_hash = {}

    for c in s:
        try:
            char_hash[c]
            return True
        except:
            char_hash = 1

    return False
