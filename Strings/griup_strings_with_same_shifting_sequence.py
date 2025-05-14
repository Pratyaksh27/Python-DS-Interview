'''
❓ Problem Statement:
Given a list of strings, group the strings that belong to the same shifting sequence.
Two strings belong to the same shifting sequence if one can be shifted to become the other, character by character.

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output:
[
  ["abc", "bcd", "xyz"],     # same pattern: +1 shift
  ["az", "ba"],              # same pattern: circular +25
  ["acef"],                  # unique shift pattern
  ["a", "z"]                 # single-letter strings
]

Why are "abc" and "xyz" grouped together?
Because both strings follow the same pattern of shifting between their letters.

Let’s break it down:
🔍 "abc":
'b' - 'a' = 1
'c' - 'b' = 1
So "abc" has the shift pattern: [1, 1]

🔍 "xyz":
'y' - 'x' = 1
'z' - 'y' = 1

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output:
[
  ["abc", "bcd", "xyz"],     # same pattern: +1 shift
  ["az", "ba"],              # same pattern: circular +25
  ["acef"],                  # unique shift pattern
  ["a", "z"]                 # single-letter strings
]
'''

def group_strings_by_shift_sequence(words):
    all_groups = []
    selected_set = set()
    for i in range(len(words)-1):
        if words[i] in selected_set:
            continue
        new_set = []
        new_set.append(words[i])
        selected_set.add(words[i])
        for j in range(i+1, len(words)):
            if words[j] in selected_set:
                continue
            if are_two_words_of_same_sequence(words[i], words[j]):
                new_set.append(words[j])
                selected_set.add(words[j])
        all_groups.append(new_set)
    return all_groups


def are_two_words_of_same_sequence(word1, word2):
    shift_sequence = []
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)-1):
        seq = ord(word1[i]) - ord(word1[i+1])%26
        shift_sequence.append(seq)
    for i in range(len(word2)-1):
        seq = ord(word1[i]) - ord(word1[i+1])%26
        if shift_sequence[i] != seq:
            return False
    return True


# word1 = 'abc'
# word2 = 'yza'
# print (are_two_words_of_same_sequence(word1, word2))
words = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
all_groups = group_strings_by_shift_sequence(words)
print(all_groups)