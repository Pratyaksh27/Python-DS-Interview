'''
INput: 'hat'
Output = [hat, hta, tha, tah, aht, ath]
Perms('ha') = ['ha', 'ah']
'''


def create_all_permutations(word, start, end):
    if start == end:
        return [word[start]]
    all_permutatations_list = []
    recursive_permutations = create_all_permutations(word, start, end-1)
    #  print(" Recursive Permutations Found :", recursive_permutations)
    for str in recursive_permutations:
        length = len(str)
        char_to_insert = word[end]
        i = 0
        while i<= length:
            new_word = insert(char_to_insert, str, i)
            all_permutatations_list.append(new_word)
            i+=1
    return all_permutatations_list

    

def insert(char, str, pos):
    # print("character to insert: ", char, " In String ", str, "at POsition ", pos)
    return str[:pos] + char + str[pos:]


word = "hat"
all_permutations = create_all_permutations(word, 0, len(word)-1)
print(all_permutations)

'''
Time Complexity: We are creating n! permutations.
How: For any combination of length n, we make a choice of a character, once a character is chosen,
it won't be repeated

so we make n * (n-1) * (n-2).... choices
=> n! permutations

Each permutaion takes o(n) time. The "return str[:pos] + char + str[pos:]" is O(n)

So Time Complexity = O(n*n!)
'''

