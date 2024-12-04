with open("2024/2nd/level.txt", encoding='utf8') as file:
    data = [line.strip('\n') for line in file.readlines()]

def list_check(list):
    '''Checks a list solely increases or decreases by no more than 3.'''
    if all(i > j for i, j in zip(list, list[1:])) == True:
        if all(j-3 <= i <= j+3 for i, j in zip(list, list[1:])):
            return True
    elif all(i < j for i, j in zip(list, list[1:])) == True:
        if all(j-3 <= i <= j+3 for i, j in zip(list, list[1:])):
            return True
    else:
        return False

def remove_item(list):
    '''Removes one item from a list and tests if it passes the list_check.'''
    for i in range(len(list)):
        new_list = list[:]
        new_list.pop(i)
        if list_check(new_list) == True:
            return True

def count(data):
    '''Counts number of lists that pass the list_check for part 1 and part 2.'''     
    part1_count = 0
    part2_count = 0
    for level in data:
        level_list = list(map(int, level.split(" ")))
        if list_check(level_list) == True:
            part1_count = part1_count + 1
            part2_count = part2_count + 1
        else:
            if remove_item(level_list) == True:
                part2_count = part2_count + 1
    return part1_count, part2_count

count1, count2 = count(data)
print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{count1} ⋆ ₊* ❅ ˚    \n\033[0m\n\n\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{count2} ⋆ ₊* ❅ ˚    \n\033[0m\n")
