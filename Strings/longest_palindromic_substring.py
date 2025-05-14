
def longest_palindromic_substring(s):
    longest_palindrome_list = []
    if (len(s)==0):
        return ''
    elif (len(s) == 1):
        return s
    for i in range(0,len(s)-1):
        temp_list = [s[i]]
        for j in range(i+1, len(s)):
            temp_list.append(s[j])
            if (isPalindrome(temp_list)):
                # print ("Palindrom Found : ", temp_list)
                if (len(temp_list) > len(longest_palindrome_list)):
                    longest_palindrome_list = temp_list[:]
                    # print(" Longest Palindrome Found so far ", str(longest_palindrome_list))
    return str(longest_palindrome_list)

def isPalindrome(temp_list):
    # print ("In IsPalindrom ", str(temp_list))
    s1 = str(temp_list)
    reverse_list = temp_list[::-1]
    s2 = str(reverse_list)
    # print ("In IsPalindrom Reverse ", str(reverse_list))
    if s1 == s2:
        return True
    return False

s1 = "babad"
s2 = "cbbd"
s3 = ''
s4 = 'a'
s5 = 'bababad'

print(" Longest Palindrome in string ", s1, " is ", longest_palindromic_substring(s1))
print(" Longest Palindrome in string ", s2, " is ", longest_palindromic_substring(s2))
print(" Longest Palindrome in string ", s3, " is ", longest_palindromic_substring(s3))
print(" Longest Palindrome in string ", s4, " is ", longest_palindromic_substring(s4))
print(" Longest Palindrome in string ", s5, " is ", longest_palindromic_substring(s5))
"""
Test cases
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""