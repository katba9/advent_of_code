import time

with open("2025/7th/map.txt") as file:
    lines = file.read().split("\n")


start_time = time.time()
start = lines[0].index("S")
current_idxs = {start}
paths_dict = {x: 0 for x in range(len(lines[0]))}
paths_dict[start] = 1
count = 0

for line in lines:
    new_idxs = set()
    for idx in current_idxs:
        if line[idx] == "^":
            count += 1
            add_idxs = [idx-1, idx+1]
            new_idxs.update(add_idxs)
            paths_dict.update({x: (paths_dict[x] + paths_dict[idx]) for x in add_idxs})
            paths_dict[idx] = 0
        else:
            new_idxs.update([idx])
    current_idxs = new_idxs


print(f"\033[44m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{count}\033[0m\33[44m  &  Part 2: \33[1m{sum(paths_dict.values())}\033[0m\33[44m ⋆ ₊* ❅ ˚   \33[1m⏱︎  -> {round((time.time() - start_time), 6)}\n\033[0m\n")