with open("2024/day_1/input.txt", "r") as f:
    lines = [line.strip().split("   ") for line in f]

left = sorted(int(line[0]) for line in lines)
right = sorted(int(line[1]) for line in lines)

# Part 1
sum_of_difference = sum(abs(l - r) for l, r in zip(left, right))
print(sum_of_difference)

# Part 2
from collections import Counter

left_count = Counter(left)
right_count = Counter(right)

total_similarity_score = sum( value * right_count[value] for value in left_count)
print(total_similarity_score)

