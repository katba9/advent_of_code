import time

with open("2025/5th/input.txt") as file:
    input = file.read()

start_time_both = time.time()

def is_fresh(i):
    for range in all_ranges:
        if range[0] <= int(i) <= range[1]:
            return i

start_time = time.time()
split = input.split("\n\n")
ingredients = [int(num) for num in split[1].split("\n")]
all_ranges = [[int(num) for num in range.split("-")] for range in split[0].split("\n")]
fresh_ingredients = list(filter(None, [is_fresh(i) for i in ingredients]))
ingredients_count = len(fresh_ingredients)
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{ingredients_count} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


start_time = time.time()
all_ranges.sort()
count = 0
highest = 0
for r in all_ranges:
    if r[0] > highest:
        count += 1 + r[1] - r[0]
        highest = r[1]
    elif r[1] > highest:
        count += r[1] - highest
        highest = r[1]

print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{count} ⋆ ₊* ❅ ˚   ⏱︎  -> {time.time() - start_time} \n\033[0m")

print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{ingredients_count}\033[0m\33[44m  &  Part 2: \33[1m{count}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time_both), 6)}\n\033[0m\n")
