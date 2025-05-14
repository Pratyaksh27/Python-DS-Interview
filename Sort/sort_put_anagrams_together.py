'''
Sort an array of strings so that anagrams are next to each other
IP = ['what', 'say', 'next', thwa, asy, def]
OP = [what, thwa, say, asy, next, def ]

TCs
IP = ['what']
IP = []
IP = ['what', 'say', 'next', thwa, asy, def]
IP = ['what', 'say', 'next', thw, as, def]
IP = ['what', 'say', 'next', thwa, asy, ahtw]
'''

def sort_anagrams(words):
    if len(words)==0 or len(words)==1:
        return words
    for i in range(len(words)-1):
        word1 = words[i]
        for j in range(i+1, len(words)):
            word2 = words[j]
            if are_anagrams(word1, word2):
                words.pop(j)
                words.insert(i+1, word2)
                break
    return words


'''
TCs
word1 = what
word = thwa

word1 = what
word = thwas

word1 = cc
word = ccc

word1 = cbb
word = bcc
'''

def are_anagrams(word1, word2):
    if (len(word1) != len(word2)):
        return False
    char_dict = {}
    for char in word1:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    
    for char in word2:
        if char in char_dict:
            char_dict[char]-=1
            if char_dict[char]==0:
                char_dict.pop(char)
        else:
            return False
    return True

words = ['what', 'say', 'next', 'thwa', 'asy', 'ahtw']
sort_anagrams(words)
print(words)
