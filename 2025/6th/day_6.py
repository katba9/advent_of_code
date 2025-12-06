import time
import math

with open("2025/6th/math.txt") as file:
    equations = file.readlines()

#Part 1
start_time = time.time()
oper_dict = {"+": sum, "*": math.prod}
equations = [num.replace("\n", "") for num in equations]
split_nums = [[n for n in num.split(" ") if n != ""] for num in equations]

total = sum([oper_dict[split_nums[-1][i]]([int(row[i]) for row in split_nums[:-1]]) 
                for i in range(len(split_nums[0]))])

print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")

#Part 2
start_time = time.time()
index_splits = [i for i, v in enumerate(equations[-1]) if v != " "] + [len(equations[-1]) + 1]

total = sum([oper_dict[equations[-1][val]]([int("".join([row[idx] for row in equations[:-1]])) for idx in range(val, index_splits[i+1]-1)])
                for i, val in enumerate(index_splits[:-1])])

print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")