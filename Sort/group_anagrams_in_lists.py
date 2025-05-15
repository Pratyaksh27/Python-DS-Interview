'''
Given a list of string list = [str1, str2,...]

Write a Sort function that creates a list of lists where each list is all anagrams
Example

IP = ['what', 'say', 'next', 'thwa', 'asy', 'def', 'what']
OP = [['what', 'thwa'], ['say', 'asy'], ['next'], ['def']]
'''

def group_by_anagrams(words):
    ret_value = []
    indices_added = set()
    for i in range(len(words)):
        if i in indices_added:
            continue
        word1 = words[i]
        new_list = [word1]
        indices_added.add(i)
        for j in range(i+1, len(words)):
            if j in indices_added:
                continue
            word2 = words[j]
            if ''.join(sorted(word1)) == ''.join(sorted(word2)):
                new_list.append(word2)
                indices_added.add(j)
        ret_value.append(new_list)
    return ret_value



words = ['what', 'say', 'next', 'thwa', 'asy', 'def']
ret = group_by_anagrams(words)
print(ret)
