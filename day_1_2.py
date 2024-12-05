import day_1_data

from collections import Counter


lines = [line.split() for line in day_1_data.DATA.split("\n") if line.strip()]
rights, lefts = zip(*[(int(r), int(l)) for r, l in lines])
left_counter = Counter(lefts)

result = sum(right * left_counter.get(right, 0) for right in rights)
print(result)