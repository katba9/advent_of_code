import time

with open("2025/3rd/banks.txt") as file:
    banks_file = file.read()
banks = [list(bank) for bank in banks_file.split("\n")]


#Part 1

def find_2_batteries(bank):
    first_b = max(bank[:-1])
    first_b_idx = bank.index(first_b)  
    second_b = max(bank[first_b_idx + 1:])
    return int(first_b + second_b)

start_time = time.time()
total = sum([find_2_batteries(bank) for bank in banks])
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


# Part 2

def find_12_batteries(bank):
    nums_list = []
    index_b = 0
    for position in range(12):
        if position == 11:
            num_range = bank[index_b:]
        else:
            num_range = bank[index_b: -(11-position)]
        b = max(num_range)
        index_b = index_b + num_range.index(b) + 1
        nums_list.extend(b)
    return int("".join(str(num) for num in nums_list))


start_time = time.time()
total = sum([find_12_batteries(bank) for bank in banks])
print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


# Part 1 & 2 together

def find_2_and_12_batteries(bank):
    nums_list = []
    index_b = 0
    for position in range(12):
        if position == 11:
            num_range = bank[index_b:]
        else:
            num_range = bank[index_b: -(11-position)]
        b = max(num_range)
        index_b = index_b + num_range.index(b) + 1
        nums_list.extend(b)
    return find_2_batteries(nums_list), int("".join(str(num) for num in nums_list))


start_time = time.time()
totals = [find_2_and_12_batteries(bank) for bank in banks]
total1, total2 = sum(num[0] for num in totals), sum(num[1] for num in totals)
print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total1}\033[0m\33[44m  &  Part 2: \33[1m{total2}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n")


# find_x_batteries function 

def find_x_batteries(bank, b_num):
    nums_list = []
    index_b = 0
    for position in range(b_num):
        if position == b_num - 1:
            num_range = bank[index_b:]
        else:
            num_range = bank[index_b: -(b_num - 1 - position)]
        b = max(num_range)
        index_b = index_b + num_range.index(b) + 1
        nums_list.extend(b)
    return int("".join(str(num) for num in nums_list))

print("Using 'find_x_batteries' function:")

start_time = time.time()
total = sum([find_x_batteries(bank, 2) for bank in banks])
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")

start_time = time.time()
total = sum([find_x_batteries(bank, 12) for bank in banks])
print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")