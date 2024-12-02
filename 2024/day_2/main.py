with open("2024/day_2/input.txt", "r") as f:
    lines = [list(map(int, line.strip().split(" "))) for line in f]

def is_safe(line):
    inc_or_dec = (line == sorted(line) or line == sorted(line, reverse=True))
    safe = True
    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i+1])
        if not 1 <= diff <= 3:
            safe = False
    return inc_or_dec and safe

#part 1

safe_count = 0
for line in lines:
    if is_safe(line):
        safe_count += 1

print("safe count", safe_count)
# ans: 371

#part 2
safe_count_2 = 0
for line in lines:
    safe = False
    for i in range(len(line)):
        line_2 = line[:i] + line[i+1:]
        if is_safe(line_2):
            safe = True
    if safe:
        safe_count_2+=1


print(safe_count_2)
#ans : 426

