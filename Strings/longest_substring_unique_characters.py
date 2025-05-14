
def longest_substring_unique_characters(s):
    if (len(s) <=1 ):
        return len(s)
    hash_set = set()
    length = 0
    for i in range (0,len(s)):
        if s[i] not in hash_set:
            hash_set.add(s[i])
        else: # We find the first non-unique character in the substrin
            if length < len(hash_set):
                length = len(hash_set)
            hash_set.clear()
            hash_set.add(s[i])
    return length

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print("Longest Substring of unique characters in string: ",s1, " is ", longest_substring_unique_characters(s1))
print("Longest Substring of unique characters in string: ",s2, " is ", longest_substring_unique_characters(s2))
print("Longest Substring of unique characters in string: ",s3, " is ", longest_substring_unique_characters(s3))
'''
Test Cases
s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

