import re
import day_3_data

result = 0  

patter = r"mul\(\d{1,3},\d{1,3}\)"
input_data = str(day_3_data.DATA)
div_do = input_data.split("do()")

for fragment in div_do:
    do, *rest = fragment.split("don't()")
    matches = re.findall(patter, do)
    for match in matches:
        a, b = match[4:-1].split(",")
        result += int(a)*int(b)

print(result)