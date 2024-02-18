def find_longest_word(input_file):

    with open(input_file, 'r') as file:
        res = ''
        lines = file.readlines()
        for word in lines:
            if len(word) > len(res):
                res = word
    return res


longest_word = find_longest_word('task.txt')
print(longest_word)