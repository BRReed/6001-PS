# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

# personal note: I relied heavily on the image supplied in the readme.md file
# in order to solve this problem. I can't find where I got it initially

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
            new_seq = sequence.replace(c, '', 1)
            new_perm = get_permutations(new_seq)
            for l in new_perm:
                perms.append(c + l)
        return perms


if __name__ == "__main__":
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
# #    sequence of length n)
    print(get_permutations('a'))
    print(get_permutations(''))
    print(get_permutations('abc'))
    print(get_permutations('abcd'))
