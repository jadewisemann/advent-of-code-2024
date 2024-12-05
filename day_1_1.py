import day_1_data

lines = day_1_data.DATA.strip().split("\n")
left_list, right_list = zip(*(map(int, line.split()) for line in lines))

left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

total_distance = (
    sum(
        abs(left - right)
        for left, right in zip(
            left_sorted, right_sorted
        )
    )
)

print(total_distance)
