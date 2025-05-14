'''
❓ Statement:
Given a string s, return True if it can become a palindrome after deleting at most one character.

Input:  "abca"
Output: True
# Remove 'b' → "aca" or remove 'c' → "aba"

Input:  "racecar"
Output: True
# Already a palindrome

Input:  "abc"
Output: False
# Can't become a palindrome by removing just one character

abcb
abab
abc

Input:  "abad"
Output: True
# Can't become a palindrome by removing just one character

Input: abcdcbba
Output: True

Input: abcdcbbba
Output: False
'''

def palindrome_with_max_1_delete(word):
    if (len(word) <= 1):
        return True
    mid = len(word)//2
    i = 0
    j = len(word)-1
    num_deletions = 0
    while i<=j:
        if word[i] != word[j]:
            num_deletions+=1
            if word[i+1] == word[j]:
                i+=1
            elif word[i] == word[j-1]:
                j-=1
            else:
                return False
        i+=1
        j-=1
    if num_deletions > 1:
        return False
    return True


word = 'abcdcbba'
print(palindrome_with_max_1_delete(word))
    












