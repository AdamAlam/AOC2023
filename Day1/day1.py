# https://adventofcode.com/2023/day/1

f = open("./Day1/input.txt", "r")

cur_sum = 0

for line in f:
    text = line.strip()
    for char in text:
        if char.isnumeric():
            first_num = char
            break

    for char in text[::-1]:
        if char.isnumeric():
            second_num = char
            break

    cur_sum += int(first_num + second_num)
    print(int(first_num + second_num))

print(cur_sum)

f.close()
