'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


# Does s2 contain a permutaion of s1 ?
# For every character in s2, if the character exists in s1 then:
#      take the substring(s2) starting from that character equal to the length of s1
#      check if that substring exists in permutations_set

def does_permutaion_exist(s1,s2):
    permutations_set = calculate_all_permutations(s1)
    for i in range(0,len(s2)):
        if s2[i] in s1:
            if (i+len(s1)-1 < len(s2)):
                s3 = s2[i: i+len(s1)]
                if s3 in permutations_set:
                    return True
    return False



def calculate_all_permutations(s1):
    permutations_set = set()
    if (len(s1)==0):
        return None
    elif (len(s1)==1):
        permutations_set.add(s1)
        return permutations_set
    
    for i in range(0,len(s1)):
        # Basically we separate out each character one at a time and then we call calculate_all_permutations on the remaining string
        c = s1[i]
        remaining_string = s1[:i] + s1[i+1:len(s1)]
        for perm in calculate_all_permutations(remaining_string):
            permutations_set.add(c+perm)
    return permutations_set


s1 = "eidbooo"   # False
s2 = "eidbaooo"  # True
s3 = "eidbooobb" # False
s4 = "eidboooab" # True
s5 = "ba"        # True
s6 = ""
s = "ab"
print(does_permutaion_exist(s,s1))
print(does_permutaion_exist(s,s2))
print(does_permutaion_exist(s,s3))
print(does_permutaion_exist(s,s4))
print(does_permutaion_exist(s,s5))
print(does_permutaion_exist(s,s6))
# calculate_all_permutations("abc")
    
