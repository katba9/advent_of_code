import time

start_time = time.time()

with open("2024/5th/instructions.txt", encoding='utf8') as file:
    intructions = file.read()

with open("2024/5th/updates.txt", encoding='utf8') as file:
    updates = file.read()

def sort_instructions(instructions):
    '''Restructures the instructions to a dictionary. Key = page, value = pages that should come afterwards.'''
    intructions_lines = intructions.splitlines()
    page_instrs = [[line[:2], line[3:]] for line in intructions_lines]
    first_instruction = [i[0] for i in page_instrs]
    first_instruction = list(set(first_instruction))
    instr_dict = {}
    for item in first_instruction:
        instr_list =[]
        for instr in page_instrs:
            if instr[0] == item:
                instr_list.append(instr[1])
        instr_dict[item] = instr_list
    return instr_dict

def which_correct(file, instr_dict):
    '''Separates the file's lists depending if they are correctly or incorrectly sorted according to the intructions.'''
    updates_lines = file.splitlines()
    correct_lines = []
    incorrect_lines = []
    for line in updates_lines:
        wrong_order = False
        line = line.split(',')
        for page in line:
            instrs = instr_dict.get(page, [])
            for page2 in line:
                if page2 in instrs:
                    if line.index(page2) > line.index(page):
                        pass
                    elif line.index(page2) < line.index(page):
                        wrong_order = True
        if wrong_order == False:
            correct_lines.append(line)
        else:
            incorrect_lines.append(line)
    return correct_lines, incorrect_lines

def sort_values(list, instr_dict):
    '''Sorts the values of lists according to the instructions.'''
    sorted_lines = []
    for line in list:
        for page in line:
            instrs = instr_dict.get(page, [])
            for page2 in line:
                if page2 in instrs:
                    if line.index(page2) < line.index(page):
                        page_to_move = line.index(page)
                        moving_page = line.pop(page_to_move)
                        new_position = line.index(page2)
                        line.insert(new_position, moving_page)
        sorted_lines.append(line)
    return sorted_lines

def find_middle_num(list):
    '''Find the middle number of a list.'''
    middle_numbers = []
    for line in list:
        middle_number = line[int((len(line)-1)/2)]
        middle_numbers.append(int(middle_number))
    return middle_numbers

instr_dict = sort_instructions(intructions)
correct_lines, incorrect_lines = which_correct(updates, instr_dict)
sorted_lines = sort_values(incorrect_lines, instr_dict)
print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{sum(find_middle_num(correct_lines))} ⋆ ₊* ❅ ˚    \n\033[0m\n\n\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{sum(find_middle_num(sorted_lines))} ⋆ ₊* ❅ ˚    \n\033[0m\n")

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")