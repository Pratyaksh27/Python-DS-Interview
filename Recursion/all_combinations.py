'''
Input: string
Output is a List of strings
'abc' = [a,b,c,ab,ac,bc,abc]
'''

def create_all_combinations(word, start, end):

    if len(word) == 0:
        return []
    
    if start == end:
        return[word[start]]
    
    recursive_combinations_list = create_all_combinations(word, start, end-1)
    all_combinations_list = []
    all_combinations_list.append(word[end])
    for str in recursive_combinations_list:
        all_combinations_list.append(str)
        new_str = str+word[end] # This take O(n) time. String Concatenation 
        all_combinations_list.append(new_str)
    
    return all_combinations_list

word = "abc"
all_combos = create_all_combinations(word, 0 , len(word)-1)
print(all_combos)


'''
Time complexity:
Correct Reasoning:
We are creating 2(power n) combinations
How: Because for each character, you’re making a choice:
-- include it, or
-- don’t include it
2 choices per character × n characters → 2ⁿ total combinations
String Concat (new_str = str+word[end]) which creates the combination is O(n)
So we have O(n*2ⁿ)


Flawed Reasoning: we call "create_all_combinations" n times (n being size of the word).
At each call we do a "for str in recursive_combinations_list:" which is O(n) too. 
And at every point we create a new string which is O(N)
So it could also be O(n3) . But that is incorrect because at each level, the size of 
recursive_combinations_list is doubling, not growing linearly.


'''