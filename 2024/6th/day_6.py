import numpy as np
import time

start_time = time.time()

with open("2024/6th/lab_map.txt", encoding='utf8') as file:
        text_data = file.read()

print(text_data)
lines = text_data.splitlines()
map = np.array([list(line) for line in lines])


start = np.where(map == "^")
x, y = start.split()
print(x)
print(y)
