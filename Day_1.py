file_path = r"C:\Users\wanke_daniel\Downloads\AdventOfCode\Day_1.txt"

list1 = []
list2 = []

with open(file_path, 'r') as file:
   for line in file.readlines():
     split_line = line.split()
     list1.append(int(split_line[0]))
     list2.append(int(split_line[1]))

# Part 1
total_dist = [abs(a-b) for a, b in zip(sorted(list1), sorted(list2))]
print(sum(total_dist))

# Part 2
similarity_scores = []

for num in list1:
  similarity_scores.append(num * list2.count(num))
print(sum(similarity_scores))
