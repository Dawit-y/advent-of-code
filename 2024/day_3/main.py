import re

with open("2024/day_3/input.txt", "r") as f:
    text = f.read().strip()

def sum_mul_characters(ls):
    result = 0
    for s in ls:
        match = re.search(r'mul\((\d+),(\d+)\)', s)
        if match:
            num1, num2 = map(int, match.groups())
            result += (num1 * num2) 
    return result

#part 1

x = re.findall(r'mul\(\d+,\d+\)', text)
part_1 = sum_mul_characters(x)
print(part_1)
#163931492

#part 2

segments = re.split(r"(don't\(\)|do\(\))", text)
accepting = True
results = []

for segment in segments:
    print(segment)
    segment = segment.strip()
    if segment == "don't()":
        accepting = False 
    elif segment == "do()":
        accepting = True  
    elif accepting:
        matches = re.findall(r'mul\(\d+,\d+\)', segment)
        results.extend(matches)

part_2 = sum_mul_characters(results)
print(part_2)
# 76911921
