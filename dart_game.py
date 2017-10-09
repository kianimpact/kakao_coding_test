import re

input = input()

pattern = r"\d+|S|D|T|\*|\#"
dict_bonus_option = {"S": "**1", 'D': "**2", "T": "**3", "#": '*-1', '*': '*2'}

array_input = re.findall(pattern, input)
array_result = list()

for value in array_input:
    if value.isdigit():
        array_result.append('+'+value)
    else:
        array_result.append(dict_bonus_option[value])
    if value == '*' and len(array_result) != 3:
        array_result.insert(len(array_result)-3, dict_bonus_option[value])

result = ''
for value in array_result:
    result += value
print(eval(result))