# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: 2:00

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    word = sequence
    if len(word) > 1:
        f_letter = sequence[0]   #first letter
        result = get_permutations(sequence[1:])
        perm_seq = []   #permutated sequence
        
        for combo in result:
            for index in range(len(word)):
                new_combo = combo[:index] + f_letter + combo[index:]
                if new_combo not in perm_seq:
                    perm_seq.append(new_combo)
        return perm_seq
    else:
        return list(word)

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    
    
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)
    
    # Test case 1
    print("----------------Test Case 1--------------------")
    test1= 'ust'
    expected =  ['ust', 'sut', 'stu', 'uts', 'tus', 'tsu']
    actual = get_permutations(test1)
    print('Expected Output:', expected)
    print('Actual Output:', get_permutations(test1))
    print("-----------------End of Test Case 1-------------")
    print("")
    
    # Test case 2
    print("----------------Test Case 2--------------------")
    test2 = 'uss'
    expected =  ['uss', 'ssu', 'sus']
    actual = get_permutations(test2)
    print('Expected Output:', expected)
    print('Actual Output:', get_permutations(test2))
    print("-----------------End of Test Case 2-------------")
    print("")
    
    
    # Test case 3
    print("----------------Test Case 3--------------------")
    test3 = 'ab'
    expected =  ['ab', 'ba']
    actual = get_permutations(test3)
    print('Expected Output:', expected)
    print('Actual Output:', get_permutations(test3))
    print("-----------------End of Test Case 3-------------")
    print("")


  





