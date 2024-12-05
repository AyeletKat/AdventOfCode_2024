# Description: Advent of Code 2024 Day 1

# Part 1
# Running time complexity: O(n*log(n)) due to use of sorting algorithm.
# (n being the number of "locations found" - lines in input.)

input = open("aof_1_1_input.txt", "r")
lines = input.readlines()
list1, list2 = [], []
# print(lines[0:4])
for line in lines:
    templist = line.split()
    list1.append(templist[0])
    list2.append(templist[1])
# print(list1[0:2])
# print(list2[0:2])

list1.sort()
list2.sort()
# print(list1[0:2])
# print(list2[0:2])
sum = 0
for i in range(len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))
print(sum)

# Part 2
from collections import Counter
# O(n)
count2 = Counter(list2)
similarity = 0
for i in range(len(list1)):
    similarity += int(list1[i])*count2[list1[i]]
print(similarity)

# Yay! It worked correctly! :)
