import time
import numpy as np

with open("2025/4th/map.txt") as file:
    roll_map = file.read()


print("Using Numpy:")


matrix = np.array([list(line) for line in roll_map.split("\n")])
directions = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
matrix_b = np.pad(matrix, pad_width=1, mode='constant', constant_values=".")


# Part 1

def access_rolls(position, value, matrix):
    count = 0
    if value != "@":
        return 0
    for d in directions:
        if matrix[position[0] + d[0]][position[1] + d[1]] == "@":
            count += 1
        if count == 4:
            return 0
    return 1
    
start_time = time.time()
counts = sum([access_rolls(idx, x, matrix_b) for idx, x in np.ndenumerate(matrix_b)])
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{counts} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")



#Part 2

start_time = time.time()
m = matrix_b.copy()
total = 0
while True:
    count_list = [access_rolls(idx, x, m) for idx, x in np.ndenumerate(m)]
    counts = sum([x for x in count_list if x == 1])
    if counts == 0:
        break
    for idx, count in enumerate(count_list):
        if count == 1:
            m[int(idx/m.shape[1])][idx % m.shape[1]] = "X"       
    total += counts

print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


#Part 1 & 2 together

start_time = time.time()
m = matrix_b.copy()
total2 = 0
count1 = True
while True:
    count_list = [access_rolls(idx, x, m) for idx, x in np.ndenumerate(m)]
    counts = sum([x for x in count_list if x == 1])
    if counts == 0:
        break
    for idx, count in enumerate(count_list):
        if count == 1:
            m[int(idx/m.shape[1])][idx % m.shape[1]] = "X" 
    total2 += counts
    if count1:
        total1 = counts
        count1 = False

print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total1}\033[0m\33[44m  &  Part 2: \33[1m{total2}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n")


print("Using a list:")


directions = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
width = len(roll_map.split("\n")[0]) + 2
positions = [y for x in [p for p in roll_map] for y in ([x] if x != '\n' else ['.', '.'])]
positions = ["." for i in range(width)] + ["."] + positions + ["." for i in range(width + 1)]


# Part 1

def access_rolls(idx, value, p_list):
    count = 0
    if value != "@":
        return 0
    for d in directions:
        if p_list[idx + (d[0]*width + d[1])] == "@":
            count += 1
        if count == 4:
            return 0
    return 1
    
start_time = time.time()
counts = sum([access_rolls(idx, value, positions) for idx, value in enumerate(positions)])
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{counts} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


#Part 2

start_time = time.time()
m = positions.copy()
total = 0
while True:
    count_list = [access_rolls(idx, value, m) for idx, value in enumerate(m)]
    counts = sum(count_list)
    if counts == 0:
        break
    for i, num in enumerate(count_list):
        if num == 1:
            m[i] = "X"       
    total += counts

print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")

# Part 1 & 2 together

start_time = time.time()
m = positions.copy()
total2 = 0
count1 = True
while True:
    count_list = [access_rolls(idx, value, m) for idx, value in enumerate(m)]
    counts = sum(count_list)
    if counts == 0:
        break
    for i, num in enumerate(count_list):
        if num == 1:
            m[i] = "X"       
    total2 += counts
    if count1:
        total1 = counts
        count1 = False

print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total1}\033[0m\33[44m  &  Part 2: \33[1m{total2}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n")
