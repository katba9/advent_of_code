import time

with open("2025/2nd/IDs.txt") as file:
    all_ranges = file.read()

num_list = [num for id_range in 
           [range.split("-") for range in all_ranges.split(",")]
            for num in range(int(id_range[0]), int(id_range[1]) + 1)]

#Part 1

def check(num):
    str_num = str(num)
    len_num = len(str_num) 
    half_str = str_num[int(len_num/2):] 

    if len_num % 2 == 0 and half_str + half_str == str_num:
        return num
    return 0 

start_time = time.time()
total = sum([check(num) for num in num_list])
print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m\n")


#Part 2

def check(num):
    str_num = str(num)
    len_num = len(str_num)

    for division in range(1, int(len_num/2) + 1):
        if len_num % division == 0 and len(set([str_num[i:i + division] for i in range(0, len_num, division)])) == 1:
            return num
    return 0

start_time = time.time()
total = sum([check(num) for num in num_list])
print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m\n")


#Part 1 & Part 2 together

def check(num):
    str_num = str(num)
    len_num = len(str_num) 
    half_num = int(len_num/2)
    half_str = str_num[half_num:]
    
    for division in range(1, half_num + 1):
        if len_num % division == 0 and len(set([str_num[i:i + division] for i in range(0, len_num, division)])) == 1:
            if half_str + half_str == str_num:
                return num, num
            return 0, num
    return 0, 0

start_time = time.time()
totals = [check(num) for num in num_list]
total1, total2 = sum(num[0] for num in totals), sum(num[1] for num in totals)
print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total1}\033[0m\33[44m  &  Part 2: \33[1m{total2}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n\n")
