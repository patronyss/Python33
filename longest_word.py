
# не маю гадки як поділити на кілька коммітів

def longest_word(lst: list):
    return max(lst, key=lambda x: len(x))


words = ['Python', 'Ruby', 'C++', 'C', 'Java', 'GO']
print(longest_word(words))
