with open('C:\\Users\\PC\\Documents\\opv1224\\tech_learn\\itstep\\python_course\\coding\\Python_Basic\\homework\\longestwordgit\\Python33\\input.txt', 'r') as file:
    content = file.readlines()
    print(max(content, key=len), end='')
    