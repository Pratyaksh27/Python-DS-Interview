'''
❓ Statement:
Write a function to check if two strings are at most one edit away (insert, remove, or replace a character)

Input: "pale", "ple"     → True   # remove 'a'
Input: "pales", "pale"   → True   # remove 's'
Input: "pale", "bale"    → True   # replace 'p' with 'b'
Input: "pale", "bake"    → False  # two edits

If diff in len is GTE 2, return False
'''

def check_if_2_strings_are_one_edit_away(word1, word2):
    diff = len(word1) - len(word2)
    if abs(diff) >= 2:
        return False
    edits = 0
    if diff == 0:
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                edits+=1
    else:
        if diff == -1:
            smaller_word = word1
            greater_word = word2
        else:
            smaller_word = word2
            greater_word = word1
        
        for i in range(len(greater_word)):
            j = i-edits
            if greater_word[i] != smaller_word[j]:
                edits+=1
        
    if (edits>=2):
        return False
    return True

word1 = 'pale'
word2 = 'bake'
print(check_if_2_strings_are_one_edit_away(word1, word2))


    