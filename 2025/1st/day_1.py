import time

with open("2025/1st/directions.txt") as file:
    instructions = file.readlines()

operation_dict = {
    "R": lambda x, y: x + y,
    "L": lambda x, y: x - y
}

count = 0
code = 50
start_time = time.time()

for instr in instructions:
    operation = operation_dict[instr[0].upper()]
    code = operation(code, int(instr[1:]))
    if code == 0 or str(code).endswith("00"):
        count = count + 1


print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{count} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m\n")


count = 0
code = 50
start_time = time.time()

for instr in instructions:
    previous_code = code
    num_change = int(instr[1:])
    operation = operation_dict[instr[0].upper()]
    code = operation(code, num_change)
    rotations = int(num_change/100)
    change = code - previous_code

    if change < 0 and previous_code > 0 and code <= (rotations)*-100:
        rotations = rotations + 1
    if change < 0 and previous_code < 0 and code <= (rotations + 1)*-100:
        rotations = rotations + 1
    if change > 0 and previous_code < 0 and code >= (rotations)*100:
        rotations = rotations + 1
    if change > 0 and previous_code > 0 and code >= (rotations + 1)*100:
        rotations = rotations + 1

    count = count + rotations

    final_num = int(str(code)[-2:])
    if code < 0:
        code = 100 - abs(final_num) if final_num != 0 else 0
    else:
        code = final_num


print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{count} ⋆ ₊* ❅ ˚   ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m\n")