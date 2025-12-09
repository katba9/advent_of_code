import time

with open("2025/8th/boxes.txt") as file:
    boxes = file.read().split("\n")


def connect_boxes(conns):
    circuits = {}
    circuit_no = 1
    for c_pair in conns:
        new_circuit = True
        connect_circuits = []

        for c_num, c_list in circuits.items():
            if not circuits:
                break
            if any(c in c_pair for c in c_list):
                if c_pair[0] not in c_list:
                    circuits[c_num].append(c_pair[0])
                if c_pair[1] not in c_list:
                    circuits[c_num].append(c_pair[1])
                connect_circuits.append(c_num)
                new_circuit = False

        if len(connect_circuits) > 1:
            [circuits[connect_circuits[0]].append(box) for box in circuits[connect_circuits[1]]
             if box not in circuits[connect_circuits[0]]]
            del circuits[connect_circuits[1]]

        if new_circuit:
            circuits[str(circuit_no)] = c_pair
            circuit_no +=1

        if len(circuits["1"]) == len(boxes):
            return c_pair
        
    return circuits


#Part 1
start_time = time.time()
boxes = [[int(x) for x in box.split(",")] for box in boxes]

closest_distance = []
for i, b1 in enumerate(boxes):
    for b2 in boxes[i+1:]:
        closest_distance.append([b1, b2]) 

conns = sorted(closest_distance, key=lambda item: (item[1][0]-item[0][0])**2 + (item[1][1]-item[0][1])**2 + (item[1][2]-item[0][2])**2)

circuits = connect_boxes(conns[:1000])
counts = [len(c) for c in circuits.values()]
counts.sort()
count = counts[-3]*counts[-2]*counts[-1]
print(f"\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{count} ⋆ ₊* ❅ ˚    ⏱︎  -> {round((time.time() - start_time), 6)} \n\033[0m")


# Part 2
start_time = time.time()
last_connection = connect_boxes(conns)
total = last_connection[0][0] * last_connection[1][0]
print(f"\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{total} ⋆ ₊* ❅ ˚   ⏱︎  -> {time.time() - start_time} \n\033[0m")
