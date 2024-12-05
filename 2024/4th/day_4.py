import numpy as np
import time

start_time = time.time()

with open("2024/4th/word_search.txt", encoding='utf8') as file:
        text_data = file.read()

#PART 1

word = "XMAS"

def find_word(row, col, direction, word, grid, counter):
    word = word[1:]
    for letter in word:
        x = row+(direction[0]*(word.index(letter)+1))
        y = col+(direction[1]*(word.index(letter)+1))
        if grid[x, y] == letter:
            pass
        else:
            return
    counter.append("x")
    return

def run_word_search(word):
    
    counter = []
    lines = text_data.splitlines()
    grid = np.array([list(line) for line in lines])
    indices = np.transpose(np.where(grid == word[0]))

    if len(word) == 1:
        return np.count_nonzero(grid == word)
                 
    for row, col in indices:

        if col+(len(word)-1) < len(grid):
            find_word(row, col, [0,1], word, grid, counter)
            if row+(len(word)-1) < len(grid):
                find_word(row, col, [1,1], word, grid, counter)
            if row-(len(word)-1) > -1:
                find_word(row, col, [-1,1], word, grid, counter)

        if col-(len(word)-1) > -1:
            find_word(row, col, [0,-1], word, grid, counter)
            if row+(len(word)-1) < len(grid):
                find_word(row, col, [1,-1], word, grid, counter)
            if row-(len(word)-1) > -1:
                find_word(row, col, [-1,-1], word, grid, counter)

        if row+(len(word)-1) < len(grid):
            find_word(row, col, [1,0], word, grid, counter)
        if row-(len(word)-1) > -1:
            find_word(row, col, [-1,0], word, grid, counter)
        
    return len(counter)

#PART 2

word = "MAS"

def find_x(row, col, counter2, grid):
    if grid[row+1, col+1] == word[0]:
        if grid[row-1, col-1] == word[2]:
            if grid[row-1, col+1] == word[0]:
                if grid[row+1, col-1] == word[2]:
                    counter2.append("x")  
                    return True
            if grid[row+1, col-1] == word[0]:
                if grid[row-1, col+1] == word[2]:
                    counter2.append("x")  
                    return True
    elif grid[row+1, col+1] == word[2]:
        if grid[row-1, col-1] == word[0]:
            if grid[row-1, col+1] == word[0]:
                if grid[row+1, col-1] == word[2]:
                    counter2.append("x")  
                    return True 
            if grid[row+1, col-1] == word[0]:
                if grid[row-1, col+1] == word[2]:
                    counter2.append("x")  
                    return True
    else:
        return False

def run_x_search():
    counter2 = []
    lines = text_data.splitlines()
    grid = np.array([list(line) for line in lines])
    indices = np.transpose(np.where(grid == word[1]))
    for row, col in indices:
        if 0 < col < 139 and 0 < row < 139:
            find_x(row, col, counter2, grid)
    return len(counter2)

counter = run_word_search(word)
counter2 = run_x_search()
print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{counter} ⋆ ₊* ❅ ˚    \n\033[0m\n\n\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{counter2} ⋆ ₊* ❅ ˚    \n\033[0m\n")

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")