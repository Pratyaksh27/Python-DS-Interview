# Does a String have all Unique characters?

def all_unique_characters(s):
    if (len(s) == 0):
        return True
    hash_set = set()
    for c in s:
        if c in hash_set:
            return False
        hash_set.add(c)
    return True

def all_unique_characters_no_extra_DS(s):
    if(len(s) == 0):
        return True
    print("Len: ",len(s))
    for i in range(0,len(s)-1):
        for j in range(i+1, len(s)):
            print("I: ",s[i]," J: ", s[j])
            if (s[i] == s[j]):
                return False
    return True


# Test Cases
s = 'sexy'
s1 = ''
s2 = 'Aaa'
assert all_unique_characters(s), " S Failed "
assert all_unique_characters(s1), " S1 Failed "
assert not all_unique_characters(s2), " S2 Failed "
assert all_unique_characters_no_extra_DS(s), " S3 Failed "
assert all_unique_characters_no_extra_DS(s1), " S4 Failed "
assert not all_unique_characters_no_extra_DS(s2), " S5 Failed "



        