
tech = ['Python', 'Ruby', 'C++', 'C', 'Java', 'GO']
with open('tech.txt', 'w', encoding='UTF-8') as file:
    print(*tech, sep='\n', file=file)


with open('tech.txt', 'r', encoding='UTF-8') as file:
    tech_list = file.readlines()

longest_word = max(tech_list, key=lambda w: len(w))

print(longest_word)