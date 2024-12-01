
f = open("2024/day_1/input.txt", "r")
lines = f.readlines()
left, right = [], []
for line in lines:
    modified_lines = line.strip().split("   ")
    left.append(int(modified_lines[0]))
    right.append(int(modified_lines[1]) )

left.sort()
right.sort()
difference_list = []
for i in range(len(left)):
    diff =  abs(left[i] - right[i]) 
    difference_list.append(diff)

sum_of_difference = sum(difference_list)
print(sum_of_difference)

# part 2

scores = []
count = 0
for i in left:
    for j in right:
        if i == j:
            count+=1
    scores.append(count * i)
    count = 0   

total_similarity_score = sum(scores)
print(total_similarity_score)