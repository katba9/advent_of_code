import time
import numpy as np

with open("2025/4th/map.txt") as file:
    roll_map = file.read()

matrix = np.array([list(line) for line in roll_map.split("\n")])
directions = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
matrix_length = matrix.shape[0]
row_dots = [["." for i in range(matrix_length)]]
column_dots = [["."] for i in range(matrix_length + 2)]

def border_matrix(matrix):
    m = np.append(matrix, row_dots, axis = 0)
    m = np.append(row_dots, m, axis = 0)
    m = np.append(m, column_dots, axis = 1)
    m = np.append(column_dots, m, axis = 1)
    return m


# Part 1

def access_rolls(position, value, matrix):
    count = 0
    if value != "@":
        return 0
    for d in directions:
        if matrix[position[0] + 1 + d[0]][position[1] + 1 + d[1]] == "@":
            count += 1
        if count == 4:
            return 0
    return 1, position
    
start_time = time.time()
border_m = border_matrix(matrix)
roll_details = [access_rolls(idx, x, border_m) for idx, x in np.ndenumerate(matrix)]
remove_0s = [x for x in roll_details if x != 0]
counts = sum(roll[0] for  roll in remove_0s)

print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{counts} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")



#Part 2

start_time = time.time()
total = 0
m = matrix.copy()
while True:
    border_m = border_matrix(m)
    roll_details = [access_rolls(idx, x, border_m) for idx, x in np.ndenumerate(m)]
    remove_0s = [x for x in roll_details if x != 0]
    counts = sum(roll[0] for  roll in remove_0s)
    if counts == 0:
        break
    for roll in remove_0s:
        m[roll[1][0]][roll[1][1]] = "X"
    total += counts

print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


#Part 1 & 2 together

start_time = time.time()
total2 = 0
m = matrix.copy()
first_count = True
while True:
    border_m = border_matrix(m)
    roll_details = [access_rolls(idx, x, border_m) for idx, x in np.ndenumerate(m)]
    remove_0s = [x for x in roll_details if x != 0]
    counts = sum(roll[0] for  roll in remove_0s)
    if counts == 0:
        break
    for roll in remove_0s:
        m[roll[1][0]][roll[1][1]] = "X"
    total2 += counts
    if first_count:
        total1 = counts
        first_count = False

print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total1}\033[0m\33[44m  &  Part 2: \33[1m{total2}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n")

