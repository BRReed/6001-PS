# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 0:
        return [sequence]
    else:
        perms = []
        for c in sequence:
            new_seq = sequence.replace(c, '')
            new_perm = get_permutations(c + new_seq)
            perms.append(new_perm)
            print(f'first: {perms}')
            for l in new_perm:
                new_seq2 = sequence.replace(l, '')
                perms.append(get_permutations(l + new_seq2))
                print(f'second: {perms}')
        return perms

print(get_permutations('abc'))

#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
# #    sequence of length n)
#     print(get_permutations('a'))
#     print(get_permutations(''))
#     print(get_permutations('abc'))

