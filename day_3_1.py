import re
import day_3_data

result = 0  

input_data = str(day_3_data.DATA)
patter = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(patter, input_data)
for match in matches:
    a, b = match[4:-1].split(",")
    result += int(a)*int(b)
    
print(result)
