import numpy as np


counter = []
word = "XMAS"
file_path = "2024/4th/word_search.txt"

def find_word(row, col, direction, word, grid):
    word = word[1:]
    for letter in word:
        x = row+(direction[0]*(word.index(letter)+1))
        y = col+(direction[1]*(word.index(letter)+1))
        if grid[x, y] == letter:
            pass
        else:
            return
    counter.append("success")
    return

def run_word_search(word, file_path):
    
    with open(file_path, encoding='utf8') as file:
        text_data = file.read()

    lines = text_data.splitlines()
    grid = np.array([list(line) for line in lines])
    indices = np.transpose(np.where(grid == word[0]))

    direction = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
                 
    for row, col in indices:
        if col+(len(word)-1) < len(grid):
            direction.pop([])
        for x, y in direction:

            if col+(len(word)-1) < len(grid):
                find_word(row, col, [0,1], word, grid)
                if row+(len(word)-1) < len(grid):
                    find_word(row, col, [1,1], word, grid)
                if row-(len(word)-1) > -1:
                    find_word(row, col, [-1,1], word, grid)

            if col-(len(word)-1) > -1:
                find_word(row, col, [0,-1], word, grid)
                if row+(len(word)-1) < len(grid):
                    find_word(row, col, [1,-1], word, grid)
                if row-(len(word)-1) > -1:
                    find_word(row, col, [-1,-1], word, grid)

            if row+(len(word)-1) < len(grid):
                find_word(row, col, [1,0], word, grid)
            if row-(len(word)-1) > -1:
                find_word(row, col, [-1,0], word, grid)
        
run_word_search(word, file_path)
print(f"Result:{len(counter)}")