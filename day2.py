# Advent of Code 2024 Day 2

# Part 1
inputf = open("aoc_day2_input.txt", "r")
lines = inputf.readlines()

increasing = True
cur_line_ok = True
counter = 0

for line in lines:
    templist = line.strip().split()
    if int(templist[0]) == int(templist[1]):
        continue
    else:
        increasing = (int(templist[0]) < int(templist[1]))
        for i in range(len(templist)-1):
            if increasing != (int(templist[i]) < int(templist[i + 1])) or (not(0 < abs(int(templist[i]) - int(templist[i + 1])) < 4)):
                cur_line_ok = False
                continue
        if cur_line_ok:
            counter += 1
        cur_line_ok = True # Reset for next iteration
print("Number of safe reports: ",  counter)
