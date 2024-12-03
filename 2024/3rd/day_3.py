import re

with open("2024/3rd/corrupt.txt", encoding='utf8') as file:
    text_data = file.read()

def multiply(data):
    list = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    multiplied_list = []
    for item in list:
        no1, no2 = item[4:-1].split(",")
        multiplied_list.append(int(no1)*int(no2))
    
    return sum(multiplied_list)

substring = "do"
start = 0
flag = True
list = []
data = text_data

while start < len(data):
    start = data.find(substring, start)
    if start == -1:
        break
    if data[start:start+5] != "don't":
        if flag == True:
            list.append(data[:start])
            data = data[start:]
            start = 0
            flag = True
        else:
            data = data[start:]
            start = 0
            flag = True
    else:
        if flag == True:
            list.append(data[:start])
            data = data[start:]
            start = 0
            flag = False
        else:
            data = data[start:]
            start = 0
            flag = False
    start += len(substring)
joined_data = "".join(list)

print(joined_data)

print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{multiply(text_data)} ⋆ ₊* ❅ ˚    \n\033[0m\n\n\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{multiply(joined_data)} ⋆ ₊* ❅ ˚    \n\033[0m\n")