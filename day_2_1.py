import day_2_data


def is_safe_report(report):
    differs = [report[i+1] - report[i] for i in range(len(report)-1)]

    if any(not  3 >= abs(differ) >= 1  or differ == 0 for differ in differs):
        return False

    if (all(differ > 0 for differ in differs) 
        or all(differ < 0 for differ in differs)):
        return True
    
    return False


safe_count = 0

input_data = [
    list(map(int, line.split())) for line 
    in day_2_data.DATA.strip().splitlines()
]

for sequence in input_data: 
    if is_safe_report(sequence):
        safe_count += 1
    
print(safe_count)

    